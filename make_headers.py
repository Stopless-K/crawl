default_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
}
def make_headers(fp, text, keys):
    if not fp and not text:
        return default_headers

    if fp:
        with open(fp, 'r') as f:
            text = f.read().split('\n')
    
    keys = set(keys)
    headers = {}
    for each in text:
        x = each.find(':')
        if x == -1:
            continue
        if each[:x] in keys:
            headers[each[:x]] = each[x+1:]
    return headers

    
