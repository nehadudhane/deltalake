# Databricks notebook source
# MAGIC %md
# MAGIC # TABLE UTILITY COMMANDS

# COMMAND ----------

# MAGIC %sql
# MAGIC Describe detail deltalakeneha.default.first_table 

# COMMAND ----------

# MAGIC %sql
# MAGIC describe extended  deltalakeneha.default.first_table

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history delta.`/Volumes/deltalakeneha/default/deltavol/dmlsink`

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from delta.`/Volumes/deltalakeneha/default/deltavol/dmlsink`

# COMMAND ----------

# MAGIC %sql
# MAGIC restore delta.`/Volumes/deltalakeneha/default/deltavol/dmlsink` 
# MAGIC to version as of 3

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from delta.`/Volumes/deltalakeneha/default/deltavol/dmlsink`
# MAGIC version as of 2

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from delta.`/Volumes/deltalakeneha/default/deltavol/dmlsink`
# MAGIC timestamp as of '2026-08-02T03:02:43.000+00:00'

# COMMAND ----------

# MAGIC %sql
# MAGIC show tblproperties deltalakeneha.default.first_table
# MAGIC     
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC show tblproperties delta.`/Volumes/deltalakeneha/default/deltavol/dmlsink`
# MAGIC

# COMMAND ----------

# MAGIC  %sql
# MAGIC  create table deltalakeneha.default.clonetb1
# MAGIC  clone delta.`/Volumes/deltalakeneha/default/deltavol/dmlsink` version as of 3
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from deltalakeneha.default.clonetb1

# COMMAND ----------

