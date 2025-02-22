# DuckDB Extension for PySpark

Since DuckDB supports only a **single writer at a time**, writing directly from PySpark can lead to **locking errors** due to Spark's multi-worker write process.  

This custom **PySpark extension** provides a reliable way to write **DataFrames to DuckDB**, ensuring smooth data transfer without concurrency issues.

## Features

- ✅ **Seamlessly write PySpark DataFrames to DuckDB**  
- ✅ **Supports `overwrite` and `append` modes**  
- ✅ **Automatically detects and adds new columns when appending data**  
- ✅ **Simple integration with PySpark's `DataFrameWriter` API**  

## Installation

You can install the package using `pip`:

```bash
pip install duckdb-spark


## Usage

Here’s how you can use the extension:

```python
from pyspark.sql import SparkSession
from duckdb_extension import DuckDBWriter

# Initialize Spark Session
spark = SparkSession.builder.appName("DuckDBExample").getOrCreate()

# Create Sample DataFrame
df = spark.createDataFrame([(1, "Alice"), (2, "Bob")], ["id", "name"])

# Write to DuckDB using the custom extension
df.write.duckdb_extension("my_db.duckdb", "users", mode="overwrite")