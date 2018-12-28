import requests


# 打印请求源文，自动猜测编码方式
# print(type(resp.text))
# print(resp.text)
# 打印网页原文，指定编码方式
# print(type(resp.content))
# print(resp.content.decode('utf-8'))
# 打印请求网页
# print(resp.url)
# # 编码方式
# print(resp.encoding)
# # 通信状态码
# print(resp.status_code)
# params = {'wd':'中国'}
# headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}
# resp = requests.get('http://www.baidu.com/s',params=params,headers=headers)
# with open('demo.html', 'w',encoding='utf-8') as fp:
#     fp.write(resp.content.decode('utf-8'))
# print(resp.url)

'''
data = {'first':'true',
        'pn':'1',
        'kd': 'python'}
headers={'Referer': 'https://www.lagou.com/jobs/list_python?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput=',
         'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
         }
resp = requests.post('https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false',data=data,headers=headers)
# with open('lagou.html', 'w',encoding='utf-8') as fp:
#     fp.write(resp.content.decode('utf-8'))
# print(resp.url)
print(resp.json())
'''
'''
代理服务器的使用
url = 'http://httpbin.org/ip'
proxy = {
    'http':'118.24.156.214:8118'
}
resp = requests.get(url,proxies=proxy)
print(resp.content.decode('utf-8'))
'''
''''
访问页面需要登录时cookie的使用
session = requests.Session()
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}
data = {
    'email': '13069562868',
    'password': 'zheng130578'
}
url = 'http://www.renren.com/PLogin.do'
session.post(url,data=data,headers=headers)
resp = session.get('http://www.renren.com/357266316/profile')
with open('demo1.html','w',encoding='utf-8') as fp:
    fp.write(resp.text)
'''
