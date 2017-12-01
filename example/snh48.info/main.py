# -*- coding: utf-8 -*-
try:
    from spider_lib import *
except:
    from __init__ import *
# from IPython import embed
import time, os, json

origin_urls = ['https://snh48.info/pics/zhanghuaijin']

#   init with headers, cache=None => no cache
# spider = Spider(fp='./example/snh48.info/headers.txt', cache=None)
spider = Spider(cache=None)


result = './result'
mkdir(result)
result = os.path.join(result, 'snh48.info')
mkdir(result)

def get_person(origin_url):
    prefix = spider.prefix(origin_url)
    def get_page(origin_url, pn):
        target = '%s/%d' % (origin_url, pn)
        tmp = spider.get_sieve(target, '<a href="/img/(.*?(png|jpg|jpeg))"')
        result = [prefix + '/img/' + each[0] for each in tmp]
        # print(result)
        if len(result) == 0:
            return None
        return {'url': target, 'results': result}

    person_file = os.path.join(result, origin_url.split('/')[-1])
    mkdir(person_file)

    args = [{'origin_url': origin_url, 'pn': pn} \
            for pn in range(1, 2)]

    
    results = []
#   single
    # for each in args:
        # res = get_page(**each)
        # if not res:
            # break
        # results += res['results']
#   mp
    mp = MP(4, get_page, args)
    mp.work()
    for each in mp.result:
        results += each['results']

    print('[SUC] total num = %d ..' % len(results))
    with open(os.path.join(person_file, 'url.json') , 'w') as f:
        json.dump(results, f)

def get_img(origin_url):
    person_file = os.path.join(result, origin_url.split('/')[-1])
    with open(os.path.join(person_file, 'url.json') , 'r') as f:
        urls = json.load(f)

    img_file = os.path.join(person_file, 'imgs')
    mkdir(img_file)
    
    args = [{'url': url, 'path': img_file} for url in urls]
#   single
    # for each in args:
        # spider.download(**each)

#   mp
    mp = MP(4, spider.download, args)
    mp.work()

def down_link():
    for origin_url in origin_urls:
        get_person(origin_url)

def down_img():
    for origin_url in origin_urls:
        get_img(origin_url)


down_link()
down_img()


