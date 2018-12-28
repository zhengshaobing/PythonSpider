from urllib import request,parse
from http.cookiejar import CookieJar

# 方式1人工手动添加cookie

# headers = {'User-Agent':' Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
#            'Cookie':'anonymid=jpjffm14-giwc4v; depovince=BJ; '
#          'jebecookies=e8b7c3f7-f4ea-449a-9663-28aa38c0cf54|||||;'
#          ' _r01_=1; ick_login=0d1164d6-fd96-4930-a35f-0f1cb0d88dc8;'
#          ' jebe_key=a06c7c82-63b6-40ca-8e18-988d34ef4f78%7Ccfcd208495d565ef66e7dff9f98764da%7C1544513432161%7C0; '
#          '_de=5AF8F2D1DA6B84BCC5D80DF1E6A95FB1; __utma=151146938.825539409.1544513621.1544513621.1544513621.1; _'
#          '_utmc=151146938; __utmz=151146938.1544513621.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E4%'
#          'BA%BA%E4%BA%BA%E7%BD%91%E7%99%BB%E5%BD%95;__utmb=151146938.1.10.1544513621; '
#          'XNESSESSIONID=abcfaWQXSLI4YeA-5lCEw; ch_id=10014; _ga=GA1.2.825539409.1544513621; '
#          '_gid=GA1.2.1538600310.1544513675; hp=601040444%2Chttp%3A%2F%2Fhdn.xnimg.cn%2Fphotos%2Fhdn521%2F20111117%2F1105%2Fh_tiny_aRFo_20a30007443a2f75.jpg%2C%E8%91%A3%E6%88%90%E9%B9%8F; Hm_lvt_46c4c9a199480813b7aa894c40e6df70=1544514014,1544514871; Hm_lpvt_46c4c9a199480813b7aa894c40e6df70=1544514871'}
# rep = request.Request(url=url,headers=headers)
# resp = request.urlopen(rep)
# # 把爬下的内容还原为网页形式，这段代码形式是固定的
# with open('renren.html','w') as fp:
#    fp.write(resp.read().decode('utf-8'))


# 方法二自动登录设置
headers = {'User-Agent':' Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}
def get_opener():
    # 1.1创建一个cookiejar对象
    cookieJar = CookieJar()
    # 1.2使用cookiejar创建一个HTTPCookieProcessor对象
    handler = request.HTTPCookieProcessor(cookieJar)
    # 1.3使用上一部创建的handler创建一个opener
    opener = request.build_opener(handler)
    return opener

def log_in(opener):
    # 1.4使用opener发送登录请求


    data = {
        'email':'13069562868',
        'password':'zheng130578'
    }
    url = 'http://www.renren.com/PLogin.do'
    rep = request.Request(url,data=parse.urlencode(data).encode('utf-8'),headers=headers)

    opener.open(rep)

def visit(opener):
    url1 = 'http://www.renren.com/357266316/profile'
    req = request.Request(url1,headers=headers)
    resp = opener.open(req)

    with open('renren1.html','w') as fp:
        fp.write(resp.read().decode('utf-8'))

if __name__ =='__main__':
    opener = get_opener()
    log_in(opener)
    visit(opener)




















































































































































