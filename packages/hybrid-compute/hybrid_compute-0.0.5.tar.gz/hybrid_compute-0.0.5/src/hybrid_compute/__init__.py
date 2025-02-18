
import json
import glob
import os
import pyarrow.parquet as pq
import pyarrow as pa
import shutil
import sqlglot
import sqlglot.expressions as exp

from collections import defaultdict
from simplekv.fs import FilesystemStore
from pyiceberg.catalog import load_catalog
from typing import Tuple

CACHE_DIR_NAME = "__hc__"
PQ_READ_BATCH_SIZE = 100_000     # number of rows
DEBUG = False


def log(msg):
    if DEBUG:
        print(msg)

class HybridCompute:
    def __init__(self, connection, catalog_config: dict):
        self._connection = connection
        self.cache_dir = os.path.join(os.getcwd(), CACHE_DIR_NAME)
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)
        self.store = FilesystemStore(os.path.join(self.cache_dir))
        self.catalog_config = catalog_config
        self.catalog = load_catalog("rest", **{
            'uri': catalog_config['uri'],
            'credential': catalog_config['credential'],
            'warehouse': catalog_config['catalog'],
            "scope": "PRINCIPAL_ROLE:ALL",
            "oauth2-server-uri": f"{catalog_config['uri']}/v1/oauth/tokens"})

    def list_remote_schemas(self):
        return self.catalog.list_namespaces()
    
    def list_remote_tables(self, schema):
        return self.catalog.list_tables(schema)
    
    def list_remote_columns(self, schema, table):
        schema = self.catalog.load_table(f"{schema}.{table}").schema()
        return [field.name for field in schema.fields]    

    def forget(self, identifier=None):
        if identifier is None:
            # delete everything
            shutil.rmtree(self.cache_dir)
        else:
            # delete store file
            store_key, schema_name, table_name = self.__parse_identifier(identifier)
            try:
                os.remove(os.path.join(self.cache_dir, store_key))
            except OSError as e:
                log(f"Warning: Could not delete store file: {store_key} | {e}")

            # delete parquet files for the table
            file_pattern = os.path.join(self.cache_dir, f"{self.catalog_config['catalog']}.{schema_name}.{table_name}.*.parquet")
            matching_files = glob.glob(file_pattern)
            for file in matching_files:
                try:
                    os.remove(file)
                    log(f"Deleted: {file}")
                except OSError as e:
                    print(f"Warning: Could not delete: {file} | {e}")

    def __parse_identifier(self, identifier: str) -> Tuple[str, str]:
        parts = identifier.split(".")
        if len(parts) == 3:
            _, schema_name, table_name = parts
        elif len(parts) == 2:
            schema_name, table_name = parts
        else:
            raise ValueError(f"Unqualified table: {identifier}")
        store_key = f"store.{self.catalog_config['catalog']}.{schema_name}.{table_name}"
        return store_key, schema_name, table_name
    
    def __create_schema(self, schema_name: str, table_name: str):
        log(f".. creating schema: {schema_name}")
        self._connection.execute(f'CREATE SCHEMA IF NOT EXISTS "{schema_name}"')

    def execute(self, query, parameters=None):        
        table_info = self.__get_table_info(query)
        
        for parsed_tbl, cols in table_info.items():
            store_key, schema_name, table_name = self.__parse_identifier(parsed_tbl)
            tbl_identifier = f"{schema_name}.{table_name}"

            try:
                existing_tbl_info = self.store.get(store_key)
                existing_cols = set(json.loads(existing_tbl_info.decode('utf-8')))
                log(f"Table already exists in local cache: {tbl_identifier}")
            except KeyError as e:
                existing_cols = None

            do_cache = False
            if existing_cols:
                if cols != existing_cols:
                    print(f".. new columns detected for table {tbl_identifier}: {cols - existing_cols}")
                    self._connection.execute(f'DROP TABLE IF EXISTS "{schema_name}"."{table_name}"')
                    self.forget(tbl_identifier)
                    do_cache = True
            else:
                self.__create_schema(schema_name, table_name)
                do_cache = True

            if do_cache:
                # download parquet files from remote
                print(f"Caching table: {tbl_identifier}")
                icb_table = self.catalog.load_table(tbl_identifier)
                # TODO: apply row filter?
                pq_files = icb_table.scan(selected_fields=cols).plan_files()
                for file_task in pq_files:
                    pq_remote_path = file_task.file.file_path
                    log(f".. downloading: {pq_remote_path}")
                    pq_reader = pq.ParquetFile(pq_remote_path)
                    pa_schema = pq_reader.schema.to_arrow_schema()
                    fields = []
                    for col in cols:
                        field = pa_schema.field(pa_schema.get_field_index(col))
                        fields.append(field)
                    schema = pa.schema(fields)
                    pq_filename = pq_remote_path.split("/")[-1]
                    pq_cache_filename = f"{self.catalog_config['catalog']}.{tbl_identifier}.{pq_filename}"
                    pq_output_path = os.path.join(self.cache_dir, pq_cache_filename)
                    with pq.ParquetWriter(pq_output_path, schema) as pq_writer:    
                        for batch in pq_reader.iter_batches(batch_size=PQ_READ_BATCH_SIZE, columns=cols):
                            pq_writer.write_batch(batch)        

                # Create local table as select from cached parquet files
                pq_cache_files =f"\"{CACHE_DIR_NAME}/{self.catalog_config['catalog']}.{schema_name}.{table_name}.*.parquet\""
                ctas_sql = f"""CREATE TABLE IF NOT EXISTS \"{schema_name}\".\"{table_name}\" AS SELECT * FROM read_parquet({pq_cache_files})"""
                self._connection.execute(ctas_sql)

                # save table info
                self.store.put(store_key, json.dumps(list(cols)).encode('utf-8'))

        result = self._connection.execute(query, parameters)
        return result

    def __get_table_info(self, query) -> dict:
        parsed = sqlglot.parse_one(query)
        table_columns = defaultdict(set)
        qualified_tables = {}  # Map of aliases to fully qualified names

        # Helper function to process a table and store its qualified name
        def register_qualified_table(table, alias=None):
            db = table.args.get("db")
            catalog = table.args.get("catalog")
            if db or catalog:
                if catalog:
                    fq_name = f"{catalog}.{db}.{table.name}"
                else:
                    fq_name = f"{db}.{table.name}"
                # Store both the table name and any alias
                if alias:
                    qualified_tables[alias] = fq_name
                table_alias = table.args.get("alias")
                if table_alias:
                    qualified_tables[table_alias.name] = fq_name
                return fq_name
            return None

        # First pass: collect all qualified tables (both from CTEs and direct queries)
        # Process CTEs if they exist
        for with_expr in parsed.find_all(exp.With):
            for cte in with_expr.expressions:
                for table in cte.this.find_all(exp.Table):
                    fq_name = register_qualified_table(table, cte.alias)
                    if fq_name:
                        qualified_tables[cte.alias] = fq_name

        # Process direct table references
        for select in parsed.find_all(exp.Select):
            for table in select.find_all(exp.Table):
                # Skip tables that are part of CTEs
                if not table.parent or not isinstance(table.parent.parent, exp.With):
                    fq_name = register_qualified_table(table)
                    if fq_name:
                        # For direct queries, store the columns right away
                        for column in select.expressions:
                            if isinstance(column, exp.Column):
                                table_columns[fq_name].add(column.name)
                            elif isinstance(column, exp.Alias):
                                this = column.this
                                if isinstance(this, exp.Column):
                                    table_columns[fq_name].add(this.name)

        # Second pass: collect columns from CTEs
        for with_expr in parsed.find_all(exp.With):
            for cte in with_expr.expressions:
                if cte.alias in qualified_tables:
                    select = cte.this
                    if isinstance(select, exp.Select):
                        fq_name = qualified_tables[cte.alias]
                        for column in select.expressions:
                            if isinstance(column, exp.Column):
                                table_columns[fq_name].add(column.name)
                            elif isinstance(column, exp.Alias):
                                this = column.this
                                if isinstance(this, exp.Column):
                                    table_columns[fq_name].add(this.name)

        # Convert sets to sorted lists
        return {tbl: set(cols) for tbl, cols in table_columns.items()}

    def __getattr__(self, name):
        # Delegate other method calls to the original connection object
        return getattr(self._connection, name)

