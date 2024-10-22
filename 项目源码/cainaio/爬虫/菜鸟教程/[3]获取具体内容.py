import os

import pandas as pd
import requests
from bs4 import BeautifulSoup

if not os.path.exists('dataset'):
    os.mkdir('dataset')

designlist = pd.read_csv('dataset/designlist.csv')
# 添加一列 content
designlist['content'] = ''

for i in designlist.iterrows():
    try:
        url = i[1]['design_url']
        # 获取网页源代码
        html = requests.get(url).text
        html = BeautifulSoup(html, 'lxml')

        # 使用BeautifulSoup定位 class="article-intro"
        html = html.find('div', class_='article-intro').text

        print({
            'id': i[1]['id'],
            'title': i[1]['title'],
            'name': i[1]['name'],
            'url': i[1]['url'],
            'design_name': i[1]['design_name'],
            'design_url': i[1]['design_url'],
            'content': html
        })

        # 将数据写入csv文件
        designlist.loc[i[0], 'content'] = html
        designlist.to_csv('dataset/designlist.csv', index=False, encoding='utf-8')
    except:
        print('error')