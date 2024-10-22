# -*- coding: utf-8 -*-
import findspark
from pyspark.sql import SparkSession

findspark.init()

hadoop_url = 'hdfs://127.0.0.1:9000/{dir}/{file}'

spark = SparkSession.builder.appName("job1").getOrCreate()
file = spark.read.csv(hadoop_url.format(dir='cainiao/dataset', file='list.csv'), header=True)
#统计每个title的数量
title_count = file.groupby('title').count()#排序
title_count = title_count.sort('count',ascending=False)
title_count.show()
#写入hadoop
title_count.write.csv(hadoop_url.format(dir='cainiao/output', file='title_count.csv'), header=True, mode='overwrite')
spark.stop()




