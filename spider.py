import sys, requests, re, os, json, shelve
from make_headers import make_headers
from lib import *
class Spider(object):
    def __init__(self, fp=None, text=None, cache=None, keys=['Accept', 'Host', 'User-Agent']):
        self.sess = requests.Session()
        self.headers = make_headers(fp, text, keys)
        cache_types = [None, 'hash', 'json']
        if cache not in cache_types:
            print('[ERR] cache is only allowed in {}'.format(cache_types))
            exit(0)

        self.cache = cache
        self.log = './run_log'
        if self.cache:
            mkdir(self.log)

    def prefix(self, url):
        return '/'.join(url.split('/')[:3 if url[:4] == 'http' else 1])

    def change_headers(self, fp=None, text=None, keys=['Accept', 'Host', 'User-Agent']):
        self.headers = make_headers(fp, text, keys)

    def post(self, url, **kwargs):
        if 'headers' not in kwargs:
            kwargs['headers'] = self.headers
        kwargs['url'] = url

        if self.cache:
            name = self.prefix(url)
            d = os.path.join(self.log, name)
            mkdir(d)

            cache_name = make_name(self.cache, kwargs)
            file_name = os.path.join(d, cache_name)

            if os.path.isfile(file_name):
                print('[OPR] found cache in %s..' % file_name)
                with shelve.open(file_name) as f:
                    return f['data']
            else:
                print('[OPR] cache not found..')
                data = requests.post(**kwargs)
                with shelve.open(file_name) as f:
                    f['data'] = data
                return data
        else:     
            return requests.post(**kwargs)
    
    def get(self, url, **kwargs):
        print('[OPR] crawling on %s ..' % url)
        if 'headers' not in kwargs:
            kwargs['headers'] = self.headers
        kwargs['url'] = url
        
        if self.cache:
            name = url.split('/')[2 if url[:4] == 'http' else 0]
            d = os.path.join(self.log, name)
            mkdir(d)

            cache_name = make_name(self.cache, kwargs)
            file_name = os.path.join(d, cache_name)

            if os.path.isfile(file_name):
                print('[OPR] found cache in %s..' % file_name)
                with shelve.open(file_name) as f:
                    return f['data']
            else:
                print('[OPR] cache not found..')
                data = requests.get(**kwargs)
                with shelve.open(file_name) as f:
                    f['data'] = data
                return data
        else:     
            return requests.get(**kwargs)
    
    def get_text(self, url, **kwargs):
        response = self.get(url, **kwargs)
        response.encoding = 'utf-8'
        return response.text

    def get_sieve(self, url, a, b=None, **kwargs):
        result = self.get_text(url, **kwargs)
        return self.sieve(result, a, b)

    def sieve(self, s, a, b=None):
        if not b:
            return re.compile(a, re.S).findall(s)
        return re.compile('%s(.*?)%s' % (a, b), re.S).findall(s)

    def get_img(self, url, suffixs=['jpg', 'png', 'gif', 'jpeg'], **kwargs):
        result = self.get_text(url, **kwargs)
        suffix = json.dumps(suffixs).replace(',', '|').replace('"', '').\
                replace('[', '(').replace(']', ')').replace(' ', '')
        return self.sieve(result, 'src="(.*?%s)' % suffix)

    def download(self, url, path, debug=False):
        if path.split('/')[-1] == url.split('/')[-1]:
            name = path
        else:
            name = os.path.join(path, url.split('/')[-1])
        print('[OPR] Downloading %s to %s ..' % (url, name))
        if not debug:
            data = self.get(url).content
            with open(name, 'wb') as f:
                f.write(data)

    def download_recursion(self, origin_url, save_path, get_files, is_dir):
        mkdir(save_path)
        q = [[origin_url, add_suffix(save_path, origin_url)]]
        vis = set()
        vis.add(origin_url)
        cur, cnt = 0, 1
        while cur < cnt:
            url, path = q[cur]
            cur += 1
            if is_dir(url):
                mkdir(path)
                urls = get_files(url)
                for each in urls:
                    if not each in vis:
                        vis.add(each)
                        q.append([each, add_suffix(path, each)])
                        cnt += 1
            else:
                self.download(url, path, debug=False)

def add_suffix(path, url):
    data = url.split('/')
    data.reverse()
    for each in data:
        if each != '':
            return os.path.join(path, each)
    print('[ERR] %s has not suffix ..' % url)
    exit(-1)

def mkdir(path):
    if not os.path.isdir(path):
        os.mkdir(path)

