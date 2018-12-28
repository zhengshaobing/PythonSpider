from lxml import etree
import requests


#
# def parse_text():
#     html = etree.HTML(text)
#     print(etree.tostring(html,encoding='utf-8').decode('utf-8'))
#
#
# def parse_file():
#
#     parser = etree.HTMLParser(encoding='utf-8')
#     html = etree.parse('demo1.html',parser=parser)
#     print(etree.tostring(html, encoding='utf-8').decode('utf-8'))
#
#
# def renren_file():
#
#     parser = etree.HTMLParser(encoding='utf-8')
#     html = etree.parse('lagou.html',parser=parser)
#     print(etree.tostring(html,encoding='utf-8').decode('utf-8'))
#
# if __name__ == '__main__':
#
#     renren_file()



'''
# 1.设置要爬取目标网站的url,params,headers等元素
url = 'https://hr.tencent.com/position.php?keywords=python&lid=2156&tid=87'
para ={
'keywords':'python',
'lid':'2156',
'tid':'87'
}
headers = {
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
'Referer':'https://hr.tencent.com/position.php?lid=2156&tid=87&keywords=%E8%AF%B7%E8%BE%93%E5%85%A5%E5%85%B3%E9%94%AE%E8%AF%8D'
}
# 2.使用requests.get(url,params,headers)命令来获取目标网站
resp = requests.get(url=url,params=para,headers=headers)
# 3.将获取到的目标网站以html文件写入本地
with open('tencent.html','w',encoding='utf-8') as fp:
    fp.write(resp.content.decode("utf-8"))
'''


'''
使用etree.parse()对文件进行读取'
'''
# 1.设置HTML文件读写器parser
parser = etree.HTMLParser(encoding='utf-8')
# 2.使用etree.parse('文件',读写器)命令来读取文件
html = etree.parse('tencent.html',parser=parser)
# print(etree.tostring(html,encoding='utf-8').decode('utf-8'))
'''使用lxml来获取HTML文件的标签
'''
# 1.获取所有tr标签
# //tr
# trs = html.xpath('//tr')
# print(len(trs))
# for tr in trs:
#     print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))
# 2.获取第二个tr标签
# trs = html.xpath('//tr[2]')
# print(etree.tostring(trs[0],encoding='utf-8').decode('utf-8'))
# 3.获取所有class等于even的tr标签
# trs = html.xpath("//tr[@class='even']")
# print(len(trs))
# for tr in trs:
#     print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))
# 4.获取所有a标签的href属性
# a_list = html.xpath("//a/@href")
# for a in a_list:
#     print(etree.tostring(a))
# 5.获取所有职位信息(纯文本)
# trs = html.xpath("//tr[position()>1]")
# positions = []
# for tr in trs:
#     # 在某个标签下,再执行xpath函数,应在//前加一个.代表是在当前元素下获取
#     href = tr.xpath(".//a/@href")[0]
#     fulurl = 'http://hr.tencent.com/' + href
#     title = tr.xpath("./td[1]//text()")[0]
#     caterage = tr.xpath("./td[2]/text()")[0]
#     numbers = tr.xpath("./td[3]/text()")[0]
#     address = tr.xpath("./td[4]/text()")[0]
#     time = tr.xpath("./td[5]/text()")[0]
#     position = {
#         'url':fulurl,
#         'title':title,
#         'caterage':caterage,
#         'numbers':numbers,
#         'address':address,
#         'time':time
#     }
#     positions.append(position)
# print(positions)