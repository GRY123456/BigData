import requests
from lxml import etree
import random
import json

'''
9
62.44.16.177:32067
118.175.93.96:47121
193.95.220.23:3128
197.234.55.217:8083
178.255.175.222:8080
114.33.189.29:41697
186.233.104.25:8080
203.77.239.18:37002
36.67.8.27:53281
'''

def spider2(url):
    proxy = [
        {
            'http': 'http://185.131.60.103:53281',
            'https': 'http://185.131.60.103:53281',
        },
    ]
    html = requests.get(url, proxies=random.choice(proxy)).text
    html = etree.HTML(html)

    # html = etree.HTML(requests.get(url).text)
    name = html.cssselect('#js_mainleft > div.b_title.clrfix > h1')
    print(name[0].text)


def spider1(url):
    html = etree.HTML(requests.get(url).text)
    names = html.cssselect(
        'body > div.qn_main_box > div > div.qn_main_ct.clrfix > div.qn_main_ct_l > div > div.listbox > ul > li')
    for name in names:
        # name = name.cssselect('div > div.titbox.clrfix > a > .cn_tit')[0]
        # print(name.text)
        sight_url = name.cssselect('div > div.titbox.clrfix > a')[0].get('href')
        spider2(sight_url)
    next_url = html.cssselect('body > div.qn_main_box > div > div.qn_main_ct.clrfix > div.qn_main_ct_l > div > div.b_paging > a.page.next')
    if next_url:
        next_url = next_url[0].get('href')
        # print(next_url)
        spider1(next_url)



with open('E:/python_work/tutorial/data_cn2.json', 'r', encoding='utf-8') as f:
    load_dict = json.load(f)
    link_index = 0
    # while link_index < len(load_dict):
    while link_index < 1:
        url = load_dict[link_index]['link'] + '-jingdian'
        link_index = link_index + 1
        spider1(url)