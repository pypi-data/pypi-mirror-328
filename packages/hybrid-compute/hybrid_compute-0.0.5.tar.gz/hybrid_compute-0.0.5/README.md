# Hybrid-Compute 
Working with cloud data is expensive and slow. We have very powerful compute resources available on our computers these days that mostly sit idle because of the move to the cloud in the past couple of decades. However, working with local data makes possible very fast iterations and a productive developer experience, as well as being cheaper than working in the cloud.

This project unlocks the potential of local compute resources by providing a way to easily and seemlessly work with cloud data on local compute resources.

# Installation
```
pip install hybrid-compute
```

# Usage
## Initialize
Wrap duckdb connection to enable caching cloud data locally. Note that Hybrid Compute currently
works with iceberg data lakes.

```python
import duckdb
import os
from hybrid_compute import HybridCompute

conn = duckdb.connect('duckdb.db')
hc = HybridCompute(conn, catalog_config={
    "uri": os.environ.get("FIVETRAN_POLARIS_URI"),
    "credential": os.environ.get("FIVETRAN_POLARIS_CREDS"),
    "catalog": os.environ.get("FIVETRAN_POLARIS_CATALOG"),
})
```

## List
You can list schemas and tables available in the cloud
```python
print(hc.list_remote_schemas())
print(hc.list_remote_tables('salesforce'))
```

## Query
Run a query against the data lake. You don't have to specify the catalog explicitly. When not
provided, the catalog name passed in via `catalog_config` will be used.

```python
results = hc.execute("SELECT learn_upon_p_lu_field_3_c, region_seg_update_c from salesforce.user").fetchall()
print(results)
```

Before the query executes, columnar data referenced in the query will be cached locally and a local table will be created within duckdb. The query will run against this local table

## Forget
You can clear the locally cached data, by table or all of it, if you like.
```python
hc.forget('salesforce.user')
```
