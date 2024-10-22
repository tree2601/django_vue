import os

import pandas as pd
import requests
from bs4 import BeautifulSoup

if not os.path.exists('dataset'):
    os.mkdir('dataset')
if not os.path.exists('dataset/designlist.csv'):
    designlist = pd.DataFrame(columns=['id', 'title', 'name', 'url', 'design_name', 'design_url'])
    designlist.to_csv('dataset/designlist.csv', index=False, encoding='utf-8')

list = pd.read_csv('dataset/list.csv')

for i in list.iterrows():
    html = requests.get(i[1]['url'])
    html = BeautifulSoup(html.text, 'lxml')
    # 使用BeautifulSoup定位 class="design"
    alist = html.find('div', class_='design').find_all('a')
    for a in alist:
        print({
            'id': i[1]['id'],
            'title': i[1]['title'],
            'name': i[1]['name'],
            'url': i[1]['url'],
            'design_name': a.text,
            'design_url': a['href']
        })
        row = pd.DataFrame({
            'id': [pd.read_csv('dataset/designlist.csv').shape[0] + 1],
            'title': i[1]['title'],
            'name': i[1]['name'],
            'url': i[1]['url'],
            'design_name': a.text,
            'design_url': 'https://www.runoob.com'+a['href']
        }, index=[0])
        row.to_csv('dataset/designlist.csv', mode='a', header=False, index=False, encoding='utf-8')
    print('-----------------------')
