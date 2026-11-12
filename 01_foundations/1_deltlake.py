# Databricks notebook source
# MAGIC %md
# MAGIC #Create Delta Table

# COMMAND ----------

# MAGIC %md
# MAGIC ### Using SQL API

# COMMAND ----------

# MAGIC %sql
# MAGIC create table deltalakeneha.default.first_table
# MAGIC (
# MAGIC     id int,
# MAGIC     salary int
# MAGIC )
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Using Delta API

# COMMAND ----------

from delta.tables import DeltaTable

# COMMAND ----------

DeltaTable.createIfNotExists(spark) \
  .tableName("deltalakeneha.default.firrstdeltaapi") \
  .addColumn("id", "INT") \
  .addColumn("salary","int")\
  .execute()

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table deltalakeneha.default.firrstdeltaapi

# COMMAND ----------

# MAGIC %md
# MAGIC #Generated Columns
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identity Columns
# MAGIC

# COMMAND ----------

from delta.tables import DeltaTable, IdentityGenerator
from pyspark.sql.types import LongType

# COMMAND ----------

from pyspark.sql.types import IntegerType, StringType

DeltaTable.create(spark) \
  .tableName("deltalakeneha.default.firrstdeltaapi") \
  .addColumn("id_col1", dataType=LongType(), generatedAlwaysAs=IdentityGenerator()) \
  .addColumn("salary", dataType=IntegerType()) \
  .addColumn("name", dataType=StringType()) \
  .execute()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Computed Columns

# COMMAND ----------

from delta.tables import DeltaTable
from pyspark.sql.types import IntegerType, StringType, LongType


# COMMAND ----------

DeltaTable.create(spark) \
  .tableName("deltalakeneha.default.firrstdeltaapi1") \
  .addColumn("salaryAfterTax", dataType=LongType(), generatedAlwaysAs="CAST((salary *0.7)as BIGINT)")\
  .addColumn("salary", dataType=IntegerType())\
  .addColumn("name", dataType=StringType())\
  .execute()

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into deltalakeneha.default.firrstdeltaapi1(salary,name) values
# MAGIC (100,'aa'),
# MAGIC (200,'bb')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from deltalakeneha.default.firrstdeltaapi1
# MAGIC