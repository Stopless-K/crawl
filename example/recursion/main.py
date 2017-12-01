# -*- coding: utf-8 -*-
try:
    from crawl import Spider
except:
    from __init__ import Spider

origin_url = ''

#   init with headers, cache=None => no cache
spider = Spider()

def is_dir(url):
    return url[-1] == '/'

def get_files(url):
    data = spider.get_sieve(url, '<li><a href="', '">')
    res = []
    for each in data:
        if each != '../':
            res.append(url + each)
    return res


spider.download_recursion('https://hevc.hhi.fraunhofer.de/svn/svn_HEVCSoftware/tags/HM-16.15/', './result/download', get_files, is_dir)





