# VectorOps

A Python library for efficiently working with geospatial vector data using DuckDB. VectorOps simplifies querying, filtering, and manipulating GeoParquet files with support for both local and S3 storage.

## Features

- Fast querying of GeoParquet files using DuckDB
- Support for both local and S3 data sources
- Spatial indexing using Hilbert curves for improved query performance
- Easy conversion between DuckDB tables and GeoDataFrames
- Partitioned writing of GeoParquet files
- SQL-based filtering and querying

## Installation
```bash
pip install vectorops
```

## Requirements
- geospatial-analysis-environment

## Quick Start
Example data can be found in Notion: https://www.notion.so/GeoDataLake-1-0-1897554f2151804d9fdcefbe4ca50f26?pvs=4#19e7554f215180d19e99db64239c0976

### Reading Data
```python
from vectorops.geoduck import GeoDuck
# Local file
geoduck = GeoDuck("./data/counties.parquet")

# S3 file
geoduck = GeoDuck("s3://bucket/path/to/counties.parquet")
```

### Querying Data
```python
# SQL queries
result = geoduck.query("SELECT NAME FROM source WHERE state = 'CA'")

# Filter and create new view
geoduck.filter("population > 1000000", view="large_counties")

# Get as GeoDataFrame
gdf = geoduck.get_dataframe("large_counties")
```

### Writing Data
```python
# Write filtered data with partitioning
geoduck.write_parquet(
    "./output/counties",
    partition_by=["state"]
)

# Write GeoDataFrame directly
from vectorops.storage import save_gdf_to_parquet
save_gdf_to_parquet(gdf, "./output/counties", partition_by=["state"])
```

## S3 Configuration

For S3 access, set the following environment variables:
```bash
export AWS_ACCESS_KEY_ID="your_access_key_id"
export AWS_SECRET_ACCESS_KEY="your_secret_access_key"
export AWS_ENDPOINT_URL="your_endpoint_url"
```

## API Reference

### GeoDuck Class

The main interface for working with geospatial data:
Key methods:
- `__init__(path)`: Initialize with path to parquet file(s)
- `filter(query, view)`: Filter data using SQL WHERE clause
- `query(sql)`: Execute custom SQL query
- `get_dataframe(view)`: Convert view to GeoDataFrame
- `write_parquet(path, view, partition_by)`: Write data to parquet

### Storage Functions

Utility functions for data storage:
- `save_gdf_to_parquet(gdf, path, partition_by)`: Save GeoDataFrame to parquet
- `write_view_to_parquet(con, view, path, partition_by)`: Write DuckDB view to parquet

## Performance

VectorOps uses several optimizations for performance:
- Hilbert curve spatial indexing for improved query speed
- DuckDB for efficient SQL operations
- Lazy loading of data
- ZSTD compression for storage efficiency
