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

```bash
from pyspark.sql import SparkSession
from duckdb_extension import register_duckdb_extension

spark = SparkSession.builder.appName("DuckDB Example").getOrCreate()

# Register the DuckDB extension
register_duckdb_extension(spark)

df=spark.read.csv("employe.csv",header=True)

# Use the custom extension to write the DataFrame to DuckDB and specify the table name
df.write.duckdb_extension(database="./company_database.duckdb", table_name="employe_tbl", mode="append")
