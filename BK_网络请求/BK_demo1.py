from urllib import request
from urllib import parse


# urlretrieve函数的用法，将一个网页上的内容保存到本地
# request.urlretrieve('http://www.baidu.com','baidu.html')
# urlencode函数的用法编码中文字符
para = {'name':'张三','age':18,'gender':'boy'}
res = parse.urlencode(para)
print(res)
# parse_qs用来解码编码后的中文字符
res = parse.parse_qs(res)
print(res)
# url = "http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=l%E5%88%98%E5%BE%B7%E5%8D%8E"
# read = request.urlopen(url)
# print(read.read())
