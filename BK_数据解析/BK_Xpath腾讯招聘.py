from lxml import etree
import requests,json,csv


Base_url = 'https://hr.tencent.com/'
Headers = {
'Referer':'https://hr.tencent.com/position.php?lid=2156&tid=87&keywords=python&start=80',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
}
Paras = {
'lid':'2156',
'tid':'87',
'keywords':'python'
}


def get_detail(url):
    '''
    抓取目标
    '''
    resp = requests.get(url, params=Paras, headers=Headers)
    text = resp.content.decode('utf-8')
    '''
    获取职位链接url
    '''
    html = etree.HTML(text)
    urls = html.xpath("//td[@class='l square']/a/@href")
    final_urls = map(lambda x: Base_url+x, urls)
    return final_urls


def page_control():
    url = 'https://hr.tencent.com/position.php?lid=2156&tid=87&keywords=python&start={}#a'
    position = []
    headers = ["职责", "职位类别", "职位",  "要求",  "地点", "招聘人数"]
    for x in range(1, 10):
        urls = url.format((x - 1) * 10)
        detail_urls = get_detail(urls)
        for detail_url in detail_urls:
            infos = spider(detail_url)
            position.append(infos)
    # 写入json文件
    # with open('腾讯招聘.json', 'w', encoding='utf-8') as fp:
    #     json.dump(position, fp, ensure_ascii=False)
    with open('腾讯招聘.csv', 'w', encoding='utf-8') as fp:
        writer = csv.DictWriter(fp, headers)
        writer.writeheader()
        writer.writerows(position)

    # print(len(position))


def spider(url):
    infos = {}
    '''详细页面抓取'''
    resp = requests.get(url,params=Paras,headers=Headers)
    text = resp.content.decode('utf-8')
    '''读取页面信息'''
    html = etree.HTML(text)
    title = html.xpath("//*[@id='sharetitle']")[0]

    infos['职位'] = title.text
    td = html.xpath("//tr[@class='c bottomline']/td")
    place = td[0].xpath('.//text()')[1]
    # for i in place:
    infos['地点'] = place
    work = td[1].xpath('.//text()')[1]
    infos['职位类别'] = work
    nums = td[2].xpath('.//text()')[1]
    infos['招聘人数'] = nums
    re = html.xpath("//ul[@class='squareli']")
    duty = re[0].xpath(".//text()")
    infos['职责'] = duty
    request = re[1].xpath('.//text()')
    infos['要求'] = request
    return infos


#
if __name__ == '__main__':
    page_control()