from lxml import etree
import requests, json, csv


Base_Url = 'https://www.dytt8.net'
Headers = {'Referer': 'https://www.dytt8.net/html/gndy/dyzz/list_23_2.html',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
}


def get_deatils(url):

    '''
        抓取目标网页信息
    '''
    # url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_1.html'
    resp = requests.get(url=url, headers=Headers)
    # 存储成文件text
    text = resp.text
    '''
    把抓取下来的数据按照一定的规则进行提取
    
    '''
    # 1.设置文件读写器
    # parser = etree.HTMLParser("gbk")
    # 2.读取目标文件信息
    html = etree.HTML(text)
    # 3.提取所需要的页面信息的url
    urls = html.xpath("//table[@class='tbspan']//a/@href")
    '''
    map(function,iterables)他是一个全局功能函数，为每一个迭代变量执行function中的处理。
    map(lambda x:Base_Url+x,urls),其中lambda是需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数。
    此条命令是指定义了一个匿名函数lambda：（Base_Url+x）,并把每个提取的urls代替x执行计算
    '''
    final_urls = map(lambda x: Base_Url+x, urls)
    # print(final_urls)
    return final_urls


def spider():
    # 1.基本的url
    basic_url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
    movies = []
    headers =['title', "style", "score",  "profiles", "actors", "down_url", "year", "country", "cover", "director"]
    for x in range(1,8):
        # 此循环使用来控制爬虫的页面数
        print('*'*30)
        print(x)
        print('*'*30)
        url = basic_url.format(x)
        # 把每页的url传入函数get_deatils()中进行提取每个电影目标的url
        detail_urls = get_deatils(url)

        for detail_url in detail_urls:
            # 此循环是用来提取每个页面中的数据详情

            movie = spars_url_page(detail_url)
            movies.append(movie)
    # 写入json为文件
    # with open('电影信息.json', 'w', encoding='utf-8') as fp:
    #     json.dump(movies, fp, ensure_ascii=False)
    # 写入为csv文件
    with open('电影信息.csv', 'w', encoding='utf-8') as fp:
        writer = csv.DictWriter(fp, headers)
        writer.writeheader()
        writer.writerows(movies)

def spars_url_page(url):
    movie = {}
    # 获取每个detail_url的页面信息
    resp = requests.get(url,headers=Headers)
    text = resp.content.decode("gbk")
    html = etree.HTML(text)
    # 提取电影标题
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']")
    # 上一步处理中title是一个列表数据无法进行译码输出，只能由普通元素转成字符串进行输出
    for i in title:
        movie['title'] = i.text
    zoom = html.xpath("//div[@id='Zoom']")[0]
    # 抓取图片
    images = zoom.xpath('.//img/@src')
    if len(images) > 0:
        cover = images[0]
    else:
        cover =''
    movie['cover'] = cover
    # scrip = images[1]
    # 抓取页面文本介绍
    infos = zoom.xpath('.//text()')
    for index,info in enumerate(infos):
        if info.startswith("◎年　　代"):
            info = info.replace("◎年　　代", "").strip()
            movie['year'] = info
        elif info.startswith("◎类　　别"):
            info = info.replace("◎类　　别　", "").strip()
            movie['style'] = info
        elif info.startswith("◎产　　地"):
            info = info.replace("◎产　　地", "").strip()
            movie['country'] = info
        elif info.startswith("◎豆瓣评分"):
            info = info.replace("◎豆瓣评分", "").strip()
            movie['score'] = info
        elif info.startswith('◎导　　演'):
            info = info.replace('◎导　　演', '').strip()
            movie['director'] = info
        elif info.startswith('◎主　　演'):
            info = info.replace('◎主　　演', '')
            actors = [info]
            for x in range(index+1, len(infos)):
                actor = infos[x].strip()
                if actor.startswith('◎'):
                    break
                actors.append(actor)
            movie['actors'] = actors
        elif info.startswith('◎简　　介 '):
            info = info.replace('◎简　　介 ', '')
            profiles = [info]
            for x in range(index+1, len(infos)):
                profile = infos[x].strip()
                if profile.startswith('【下载地址】'):
                    break
                    profiles.append(profile)
            movie['profiles'] = profiles
    #             # print(profile)
    down_url = html.xpath("//td[@style='WORD-WRAP: break-word']/a/@href")
    movie['down_url'] = down_url
    return movie
    # for x in cover:
    #      print()
    #print(movie)
# '''
# 抓取目标网页信息
# '''
# url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_1.html'
#
# resp = requests.get(url=url,headers=headers)
# # 存储成文件text
# text = resp.content.decode('gb2312')
#
# '''
# 把抓取下来的数据按照一定的规则进行提取
# '''
# # 1.设置文件读写器
# # parser = etree.HTMLParser("gbk")
# # 2.读取目标文件信息
# html = etree.HTML(text)
# # 3.提取所需要的页面信息
# uls = html.xpath("//table[@class='tbspan']//a/@href")
#
# for ul in uls:
#     print(base_url+ul)


if __name__ == '__main__':
     spider()