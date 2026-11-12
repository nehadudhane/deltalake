# Databricks notebook source
# MAGIC %md
# MAGIC # UNIFORM
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC Create table deltalakeneha.default.unitbl
# MAGIC using delta tblproperties(
# MAGIC     'delta.enableIcebergCompatV2'='True',
# MAGIC     'delta.universalFormat.enabledFormats'='iceberg');
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into deltalakeneha.default.unitbl