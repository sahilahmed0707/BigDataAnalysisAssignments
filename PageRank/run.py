import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/home/sahil/spark/spark-3.3.0-bin-hadoop3"
import findspark
findspark.init()
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").getOrCreate()
sc = spark.sparkContext

rdd = sc.textFile('network.txt').persist()

def computeContribs(neighbors, rank):
    for neighbor in neighbors:
        yield (neighbor, rank/len(neighbors))

linksRDD= rdd.map(lambda x:tuple(x.split(" "))).map(lambda x:(x[0],[x[1]])).reduceByKey(lambda x, y: x+y).collect()
print(linksRDD)
linksRDD2=sc.parallelize (linksRDD)
ranksRDD=linksRDD2.map(lambda x:(x[0],1.0)).collect()
print(ranksRDD)

ranksRDD2=sc.parallelize(ranksRDD)
for iteration in range(10): 
  # calculate the contribution of each page's outgoing link
  contribs=linksRDD2.join(ranksRDD2).map(lambda x:x[1]).flatMap(lambda x: computeContribs(x[0],x[1]))
  # update each page's page rank by summing up all incoming link's contribution
  ranksRDD2 =contribs.reduceByKey(lambda x,y:x+y)

ranksRDD2.collect()
