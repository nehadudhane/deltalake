# Databricks notebook source
data=[(1,100,'xyz',1),(9,200,'bb',1),(10,300,"cc",1)]

df=spark.createDataFrame(data,['CUST_ID','income','name','tip'])

display(df)

# COMMAND ----------

df.write.format("delta")\
    .mode("append")\
    .save("/Volumes/deltalakeneha/default/deltavol/schemalevel/")

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Enable column mapping and rename the column
# MAGIC ALTER TABLE delta.\`/Volumes/deltalakeneha/default/deltavol/schemalevel/\`
# MAGIC SET TBLPROPERTIES (
# MAGIC     'delta.minReaderVersion' = '2',
# MAGIC     'delta.minWriterVersion' = '5',
# MAGIC     'delta.columnMapping.mode' = 'name');
# MAGIC
# MAGIC ALTER TABLE delta.\`/Volumes/deltalakeneha/default/deltavol/schemalevel/\`
# MAGIC RENAME COLUMN name to customer_name;

# COMMAND ----------

# MAGIC %sql
# MAGIC select *  from  delta.\`/Volumes/deltalakeneha/default/deltavol/schemalevel/\`

# COMMAND ----------

