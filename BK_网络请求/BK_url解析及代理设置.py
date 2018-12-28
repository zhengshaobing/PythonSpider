from urllib import request,parse


# url ='https://www.baidu.com'
#
# result = parse.urlparse(url)
# result1 = parse.urlsplit(url)
# print(result1)
#
# url ='https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
#
# # data = request.urlopen(url)
# # print(data.read())
# headers = {"User-Agent":" Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
#            "Referer":"https://www.lagou.com/jobs/list_python?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput="}
# data = {
#     'first':'true',
#     'pn':1,
#     'kd':'python'
# }
# resp = request.Request(url,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST')
# result = request.urlopen(resp)
# print(result.read().decode('utf-8'))
# 不使用代理ip
url = 'http://httpbin.org/ip'
resp = request.urlopen(url)
print(resp.read())
# 使用代理ip变化
# 1.使用proxyhandler,传入一个代理ip
handler = request.ProxyHandler({'http':'106.2.1.5:3128'})
# 2.使用已创建的handler构建一个opener
opener = request.build_opener(handler)
# 3.使用opener发送请求
resp = opener.open(url)
print(resp.read())
