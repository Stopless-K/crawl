# -*- coding: utf-8 -*-
try:
    from spider_lib import Spider
except:
    from __init__ import Spider

import re
origin_url = 'http://www.80s.tw/ju/21781?LMCL=p_JJEY'

#   init with headers, cache=None => no cache
spider = Spider()
res = re.compile('<a rel="nofollow" href="(thunder://.*?)" thunderrestitle="(.*?)"').findall(spider.get_text(origin_url))

for each in res:
    print(each[1], each[0])




