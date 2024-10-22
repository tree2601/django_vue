import os

import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.runoob.com/'

if not os.path.exists('dataset'):
    os.mkdir('dataset')
if not os.path.exists('dataset/list.csv'):
    list = pd.DataFrame(columns=['id','title', 'name', 'url'])
    list.to_csv('dataset/list.csv', index=False, encoding='utf-8')

# 获取网页源代码
html = requests.get(url).text
html = BeautifulSoup(html, 'lxml')
#使用Xpath定位 //div[@class="col middle-column-home"]/div
#使用BeautifulSoup定位
html = html.find('div', class_='col middle-column-home').find_all('div')

for i in html:
    title = i.find('h2').text
    alist = i.find_all('a')
    for a in alist:
        print({
            'title': title,
            'name': a.text,
            'url': a['href']
        })
        # 先根据url查询csv文件，如果存在则不写入
        if pd.read_csv('dataset/list.csv').query('url == "%s"' % a['href']).shape[0] > 0:
            continue
        # 将数据写入csv文件
        row = pd.DataFrame({
            'id': [pd.read_csv('dataset/list.csv').shape[0] + 1],
            'title': title,
            'name': a.text,
            'url': 'https:'+a['href']
        }, index=[0])
        row.to_csv('dataset/list.csv', mode='a', header=False, index=False, encoding='utf-8')
    print('-----------------------')
