# -*- coding: utf-8 -*-
try:
    from spider_lib import *
except:
    from __init__ import *
from IPython import embed
import time, os, json

origin_urls = ['http://www.snh48club.com/image/member239']

#   init with headers, cache=None => no cache
spider = Spider(fp='./example/snh48club/headers.txt', cache=None)


result = './result'
mkdir(result)
result = os.path.join(result, 'snh48club')
mkdir(result)

def get_person(origin_url):
    prefix = spider.prefix(origin_url)
    def get_page(origin_url, pn):
        target = '%s/%d' % (origin_url, pn)
        result = spider.get_sieve(target, '<img src="', '"')[1:]
        if len(result) == 0:
            return None
        return {'url': target, 'results': result}

    person_file = os.path.join(result, origin_url.split('/')[-1])
    mkdir(person_file)

    args = [{'origin_url': origin_url, 'pn': pn} \
            for pn in range(1, 1000)]

    mp = MP(1, get_page, args)
    mp.work()
    

    results = []
    for each in mp.result:
        results += each['results']
    with open(os.path.join(person_file, 'url.json') , 'w') as f:
        json.dump(results, f)

def get_img(origin_url):
    person_file = os.path.join(result, origin_url.split('/')[-1])
    with open(os.path.join(person_file, 'url.json') , 'r') as f:
        urls = json.load(f)

    img_file = os.path.join(person_file, 'imgs')
    mkdir(img_file)
    
    spider.download('http://img.snh48club.com/snh48club/images/upload/day_171119/201711190341529721.jpg', img_file)
    args = [{'url': url, 'path': img_file} for url in urls]
    mp = MP(1, spider.download, args)
    mp.work()

def down_link():
    for origin_url in origin_urls:
        get_person(origin_url)

def down_img():
    for origin_url in origin_urls:
        get_img(origin_url)


# down_link()
spider.change_headers(fp='./example/snh48club/headers_img.txt')
down_img()


