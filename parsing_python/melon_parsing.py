import requests
import json
from bs4 import BeautifulSoup
from collections import OrderedDict

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
response = requests.get('https://www.melon.com/chart/index.htm', headers=header) #멜론은 헤더 추가해줘야 접근가능함
html = response.text

soup = BeautifulSoup(html, 'html.parser')

tmp_title = soup.find_all("div", {"class": "ellipsis rank01"})
tmp_singer = soup.find_all("div", {"class": "ellipsis rank02"})

title = []
singer = []

for i in tmp_title:
    title.append(i.find('a').text)
for j in tmp_singer:
    singer.append(j.find('a').text)


total_rank = len(title)

json_data = {}
for i in range(total_rank):
    json_data[(i+1)] = {'singer':singer[i], 'title':title[i]}

with open("file_path",'w',encoding='utf-8') as outfile:
    # json.dump(json_data,outfile,indent='\t',ensure_ascii=False)
    json.dump(json_data, outfile, indent='\t', ensure_ascii=False)
