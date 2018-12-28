from lxml import etree
import requests


# def get_html():
'''
 抓取目标网站
'''
url = 'https://movie.douban.com/cinema/nowplaying/beijing/'
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
    'Referer':'https://www.douban.com/'
    }
resp = requests.get(url,headers=headers)
# print(resp.content.decode('utf-8'))
text = resp.content.decode('utf-8')
# return text


# def html_process(text):
'''
把抓取下来的数据按照一定的规则进行提取
'''
# 1.选定HTML读写器
parser =etree.HTMLParser(encoding='utf-8')
# 2.etree.HTML处理文档
html = etree.HTML(text,parser=parser)
ul = html.xpath("//ul[@class='lists']")[0]
# print(etree.tostring(ul,encoding='utf-8').decode('utf-8'))
lis = ul.xpath('./li')
movie_informations = []
for li in lis:
   title = li.xpath("@data-title")[0]
   score = li.xpath("@data-score")[0]
   duration = li.xpath("@data-duration")[0]
   region = li.xpath("@data-region")[0]
   director= li.xpath("@data-director")[0]
   actors = li.xpath("@data-actors")[0]
   image = li.xpath('.//img/@src')[0]
   information ={
       'title':title,
       'score':score,
       'duration':duration,
       'region':region,
       'director':director,
       'actors':actors,
       'image':image
   }

   movie_informations.append(information)
print(movie_informations)
# if __name__=='__main':
#     la= get_html()
#     html_process(la)
