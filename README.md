# Delta Lake with Databricks — Hands-On Notebooks

A collection of Databricks notebooks demonstrating **Delta Lake** operations: table creation, transaction log inspection, schema enforcement and evolution, MERGE upserts, table history and time travel, cloning, Change Data Feed, and introductory Delta UniForm settings.

The examples are organized by topic so each concept can be reviewed independently. Several notebooks build on tables and Volume locations created earlier in the exercises.

## Technology stack

- Databricks and Delta Lake
- PySpark and Spark DataFrame API
- Databricks SQL
- `DeltaTable` Python API
- Unity Catalog tables and Volumes, as referenced in the source

## Repository structure

```text
deltalake/
├── README.md
├── 01_foundations/
│   ├── 1_deltlake.py
│   └── 2_deltalake.py
├── 02_schema_management/
│   ├── 3_deltalake.py
│   └── 5_deltalake.py
├── 03_data_operations/
│   └── 4_deltalake.py
├── 04_table_utilities/
│   └── 6_deltalake.py
├── 05_change_data_feed/
│   └── 7_deltalake.py
└── 06_universal_format/
    ├── 8_deltalake.py
    └── 9_deltalake.py
```

## Notebook guide

| Notebook | Concepts covered |
| --- | --- |
| [`1_deltlake.py`](01_foundations/1_deltlake.py) | Delta table creation with SQL and Delta API, identity columns, computed columns |
| [`2_deltalake.py`](01_foundations/2_deltalake.py) | Writing Delta data and inspecting a transaction-log JSON file |
| [`3_deltalake.py`](02_schema_management/3_deltalake.py) | Schema enforcement, `mergeSchema`, `overwriteSchema`, Delta reads |
| [`4_deltalake.py`](03_data_operations/4_deltalake.py) | Inserts, updates, and `MERGE`-based upserts |
| [`5_deltalake.py`](02_schema_management/5_deltalake.py) | Column mapping and renaming columns |
| [`6_deltalake.py`](04_table_utilities/6_deltalake.py) | Table details, history, restore, time travel, properties, cloning |
| [`7_deltalake.py`](05_change_data_feed/7_deltalake.py) | Enabling Change Data Feed and querying changes |
| [`8_deltalake.py`](06_universal_format/8_deltalake.py) | Delta UniForm / Iceberg compatibility settings |
| [`9_deltalake.py`](06_universal_format/9_deltalake.py) | Empty notebook export retained for completeness |

## Learning topics

### Delta Lake foundations
Create managed Delta tables using SQL and the Delta API, including generated columns. Write DataFrames to Delta paths and explore the transaction log under `_delta_log`.

### Schema management and data operations
Experiment with schema enforcement and evolution, update records, and apply upserts with the Delta Lake MERGE API.

### Versioning and change tracking
Inspect table history, restore and query historical versions, clone tables, and enable Change Data Feed to review changes.

### Universal Format
Explore Delta table properties for Iceberg compatibility. **Notebook 8 has an unfinished INSERT statement and notebook 9 is blank.** They are retained as originally supplied rather than represented as completed examples.

## Using the notebooks

These are Databricks Python notebook exports containing `%sql` and `%md` cells. Import the files into a compatible Databricks workspace to run them.

The original code references the `deltalakeneha` catalog, its `default` schema, and paths under `/Volumes/deltalakeneha/default/deltavol/`. Those references are environment-specific; your own environment must provide matching tables and storage locations or be configured accordingly.

This repository demonstrates hands-on Delta Lake features, not a scheduled production ETL pipeline. Execution results and automated test outcomes are not included.

## Author

**Neha Dudhane** — [GitHub](https://github.com/nehadudhane)
