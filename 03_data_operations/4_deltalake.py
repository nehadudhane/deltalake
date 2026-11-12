# Databricks notebook source
# MAGIC %md
# MAGIC # DML
# MAGIC

# COMMAND ----------

data=[(1,100,'aa',1),(2,200,'bb',1),(3,300,"cc",1),(4,400,"dd",1)]

df=spark.createDataFrame(data,['CUST_ID','income','name','tip'])


df.write.format("delta")\
    .mode("append")\
    .save("/Volumes/deltalakeneha/default/deltavol/dmlsink/")

# COMMAND ----------

data=[(5,100,'aa',1),(6,200,'bb',1),(7,300,"cc",1),(8,400,"dd",1)]

df=spark.createDataFrame(data,['CUST_ID','income','name','tip'])


df.write.format("delta")\
    .mode("append")\
    .save("/Volumes/deltalakeneha/default/deltavol/dmlsink/")

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from delta.\`/Volumes/deltalakeneha/default/deltavol/dmlsink/\`

# COMMAND ----------

# MAGIC %md
# MAGIC ### update

# COMMAND ----------

# MAGIC %sql
# MAGIC update delta.\`/Volumes/deltalakeneha/default/deltavol/dmlsink/\` 
# MAGIC set income=1000 where CUST_ID=5

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from delta.\`/Volumes/deltalakeneha/default/deltavol/dmlsink/\`

# COMMAND ----------

# MAGIC %md
# MAGIC # UPSERT

# COMMAND ----------

data=[(1,100,'xyz',1),(9,200,'bb',1),(10,300,"cc",1)]

df=spark.createDataFrame(data,['CUST_ID','income','name','tip'])

display(df)

# COMMAND ----------

from delta.tables import DeltaTable

# COMMAND ----------

dlt_obj =DeltaTable.forPath(spark,"/Volumes/deltalakeneha/default/deltavol/dmlsink/")

dlt_obj.alias("trg").merge(df.alias("src"),"trg.CUST_ID= src.CUST_ID")\
    .whenMatchedUpdateAll()\
    .whenNotMatchedInsertAll()\
    .execute()


# COMMAND ----------

# MAGIC %sql
# MAGIC select * from delta.\`/Volumes/deltalakeneha/default/deltavol/dmlsink/\`

# COMMAND ----------

