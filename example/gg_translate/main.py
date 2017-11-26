# -*- coding: utf-8 -*-
try:
    from spider_lib import Spider
except:
    from __init__ import Spider
from IPython import embed

languages = {'chinese': 'zh', 'english': 'en', 'spanish': 'spa', 'japanese': 'jp'}


origin_url = 'http://fanyi.baidu.com/v2transapi'

#   init with headers, cache=None => no cache

def translate(words, sl, tl):
    res = spider.post(origin_url, data={
        'from': languages[sl], 'to': languages[tl],
        'query': words, 
        'transtype': 'realtime',
        'simple_means_flag': 5,
    })
    data = res.json()['trans_result']['data'][0]['dst']
    return data


spider = Spider(fp='./example/gg_translate/headers.txt')


def cycle_translate(words, sl, tl):
    gen = translate(words, sl, tl)
    ch_gen = translate(words, sl, 'chinese')
    recon = translate(gen, tl, sl)
    ch_recon = translate(gen, tl, 'chinese')
    result = {'gen': gen, 'ch_gen': ch_gen, 'recon': recon, 'ch_recon': ch_recon}
    print(result, '\n')

while True:
    words = input('Words: ')
    if not words:
        break
    cycle_translate(words, 'english', 'spanish')
    cycle_translate(words, 'spanish', 'english')

    cycle_translate(words, 'english', 'japanese')
    cycle_translate(words, 'japanese', 'english')







