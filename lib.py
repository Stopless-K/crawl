import hashlib, json, os

def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def mkdir(path):
    if not os.path.isdir(path):
        os.mkdir(path)


def make_name(method, kwargs):
    data = json.dumps(kwargs)
    if method == 'hash':
        data = md5(data)
    return data
