import requests
from bs4 import BeautifulSoup
from pyecharts import Bar
import json,csv

Headers = {
'Referer':'http://www.weather.com.cn/forecast/',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
}
All_data = []


def Main():
    a_list = []
    urls = {'http://www.weather.com.cn/textFC/hb.shtml#',
            'http://www.weather.com.cn/textFC/db.shtml#',
            'http://www.weather.com.cn/textFC/hd.shtml#',
            'http://www.weather.com.cn/textFC/hz.shtml#',
            'http://www.weather.com.cn/textFC/hn.shtml#',
            'http://www.weather.com.cn/textFC/xb.shtml#',
            'http://www.weather.com.cn/textFC/xn.shtml#'

            }
    for url in urls:
        Parse_Page(url)
    # 升序排列 reserve = False
    All_data.sort(key=lambda data:data['最低气温'], reverse=False)
    headers = ['最低气温', '城市']
    data = All_data[0:10]
    # print(data)
    cities = list(map(lambda x:x['城市'],data))
    tempreture = list(map(lambda x: x['最低气温'], data))
    # print(cities)
    # print(tempreture)
    chart = Bar("中国天气最低气温排行")
    chart.add("",cities,tempreture)
    chart.render('tempreture.html')

    # 降序排列 reserve = True
    # All_data.sort(key=lambda data: data['最低气温'], reverse=True)
    # data1 = All_data[0:10]
    # print(data1)
    '''写作json文件'''
    # with open('城市气温.json', 'w', encoding='utf-8') as fp:
    #     json.dump(data, fp, ensure_ascii=False)
    '''写作csv文件'''
    with open('城市气温.csv', 'w', encoding='utf-8') as fp:
        writer = csv.DictWriter(fp,headers)
        writer.writeheader()
        writer.writerows(data)


def Parse_Page(url):

    infos = {}
    resp = requests.get(url,headers=Headers)
    text = resp.content.decode('utf-8')
    bs = BeautifulSoup(text,'lxml')
    conMidtab = bs.find('div',class_='conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index,tr in enumerate(trs):
            tds = tr.find_all('td')
            if index == 0:
                city_td = tds[1]
            else:
                city_td = tds[0]
            city = list(city_td.stripped_strings)[0]
            infos['城市'] = city
            tempreture = list(tds[-2].stripped_strings)[0]
            infos['最低气温'] = int(tempreture)
            All_data.append({'城市':city,'最低气温':int(tempreture)})
             # print(infos)
        #print('*'*30)


if __name__ == '__main__':
    Main()