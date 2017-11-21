# -*- coding: utf-8 -*-
try:
    from spider_lib import Spider
except:
    from __init__ import Spider

origin_url = 'http://www.meijutt.com/content/meiju23099.html'

#   init with headers, cache=None => no cache
spider = Spider(fp='./example/meijutt/headers.txt', cache='hash')


data = spider.get_sieve(origin_url, '<div class="down_list"><ul>', '</ul></div>')

for each_table in data[0:3:2]:
    items = spider.sieve(each_table, '<li', '</li>')
    for item in items:
        value = spider.sieve(item, 'file_name="', '"')[0]
        link = spider.sieve(item, '<a href="', '">')[0]
        print(value, link)



