# Crawl
Crawing Utils  
You can use it as submodule or the main project.
##  introduction
### Class MP
#### multiprocessing
	file: ./multiprocess.py  
	you can change import to use 	threading
#### initialize
	mp = MP(num_process, func, data)
#### run
	mp.work()
#### Example
```python
e.g.
	def func(input_a, input_b):
		print(input_a, input_b)
		return input_a + input_b	
	data = [{'input_a': i, 'input_b': i} for i in range(10)]
	mp = MP(4, func, data)
	mp.work()
	result = mp.result
		
	
	see ./example/snh48.info for details
```
### Class Spider
#### spider
	file: ./spider.py
#### initialize
	spider = Spider(fp='./headers.txt', text='Accept:....', cache=None, keys=['Accept', ...'])
	+fp: file path of headers
	+text: text of headers
		-One of them is enough
	+cache: [None, 'hash', 'json']
		-None: for no cache
		-hash: save url in local use md5 as name
		-json: save url in local use json as name
	+keys: load keys from headers
		-[]: load all key
		-['xx', 'aa']: load 'xx', 'aa' only
#### run
##### spider.post
	request.post
##### spider.get
	request.get 
	if no headers, it will use spider.headers
##### spider.change_headers
	spider.change_headers(fp, text, keys)
	change spider.headers
##### spider.get_text
	return text
##### spider.get_sieve
	return text in url satisfy a(.*?)b or a (re)
##### spider.get_img
	spider.get_img(url, suffixs)
	suffixs default: ['jpg', 'png', 'gif', 'jpegf']
##### spider.download
	spider.download(url, path)
##### spider.download_recursion
	spider.download_recursion(origin_url, save_path, get_files, is_dir)
	get_files: function to get all files in current url
	is_dir: function to determine whether current url is a director
	
	see ./example/recursion/main.py for details
	

##  issues


##  requirement
1\*.  a <a href='https://www.google.com/search?&q=computer&oq=computer'>computer</a> with the <a href='http://paste.ubuntu.com/26010673/'>Internet</a>  
2\*.  <a href='https://www.python.org/downloads/'>Python3.0+</a>  (not sure wether python2.0+ works)  
3.  pip3    (if you wanna install extra package of python)  
4.  Make    (only for Makefile, you can choose not to use it)  
(\* means what you must have)  

##  example
see ./example/* for details

##  install
```shell
make install    #   see Makefile for details
```
