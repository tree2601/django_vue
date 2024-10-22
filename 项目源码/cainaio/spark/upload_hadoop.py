import os

# 执行命令hadoop fs -ls / 查看是否创建成功

hadoop_url = 'hdfs://127.0.0.1:9000/{dir}/{file}'
hadoop_upload_command = 'hadoop fs -put {local_path} {hadoop_path}'


def upload_file_to_hadoop(local_path, hadoop_path):
    os.system(hadoop_upload_command.format(local_path=local_path, hadoop_path=hadoop_path))


def loadFileList(dir):
    return os.listdir(dir)


commands = [
    'hadoop fs -mkdir hdfs://127.0.0.1:9000/cainiao',
    'hadoop fs -mkdir hdfs://127.0.0.1:9000/cainiao/dataset',
    'hadoop fs -mkdir hdfs://127.0.0.1:9000/cainiao/output',

]

# 创建文件夹
for command in commands:
    print(f'执行命令：{command}')
    os.system(command)

# 上传文件到hadoop
print('正在上传文件：list.csv')
upload_file_to_hadoop('dataset/list.csv',
                      hadoop_url.format(dir='cainiao/dataset', file='list.csv'))
print('正在上传文件：designlist.csv')
upload_file_to_hadoop('dataset/cainiao.csv',
                      hadoop_url.format(dir='cainiao/dataset', file='designlist.csv'))
upload_file_to_hadoop('dataset/cainiao_based.csv',
                      hadoop_url.format(dir='cainiao/dataset', file='cainiao_based.csv'))

