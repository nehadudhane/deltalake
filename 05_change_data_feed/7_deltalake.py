# Databricks notebook source
# MAGIC %sql 
# MAGIC alter table deltalakeneha.default.clonetb1
# MAGIC set tblproperties (delta.enableChangeDataFeed = true)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from deltalakeneha.default.clonetb1

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into deltalakeneha.default.clonetb1
# MAGIC values (10,100,'zz',1)

# COMMAND ----------

# MAGIC %sql
# MAGIC delete from deltalakeneha.default.clonetb1
# MAGIC where CUST_ID=3

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history deltalakeneha.default.clonetb1

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from table_changes('deltalakeneha.default.clonetb1',1)

# COMMAND ----------

