import requests
import time,re,json
from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
#
# headers = {
#     'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
#     'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/71.0.3578.80Safari/537.36'
# }
# '''
# 传统的爬虫方法
# '''
#
#
# def main():
#     url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
#
#     data = {
#         'first': 'false',
#         'pn': '1',
#         'kd': 'python'
#     }
#     for x in range(1, 11):
#         data['pn'] = x
#         resp = requests.post(url, headers=headers, data=data)
#         # json方法:如果返回值是json数据。那么此方法会自动的load成字典
#         # print(resp.json())
#         result = resp.json()
#         positions = result['content']['positionResult']['result']
#         for position in positions:
#             positionId = position['positionId']
#             page_url = 'https://www.lagou.com/jobs/%s.html' % positionId
#             parse_page(page_url)
#             break
#         break
#
#
# def parse_page(url):
#     resp = requests.get(url, headers=headers)
#     text = resp.text
#     html = etree.HTML(text)
#     position_name = html.xpath('//span[@class="name"]/text()')[0]
#     body = html.xpath('//p/span/text()')
#     salary = body[0]
#     worke_place = re.sub(r'[\s/]', '', body[1]).strip()
#     work_experience = re.sub(r'\s/', '', body[2]).strip()
#     education = re.sub(r'\s/', '', body[3]).strip()
#     style = re.sub(r'\s/', '', body[4]).strip()
#     work_detail = "".join(html.xpath("//div[@class='job-detail']/p/text()"))
#     print(work_detail)
#
#
# if __name__ == '__main__':
#     main()
'''
使用selenium进行爬取数据
'''


class LagouSpider(object):
    driver_path = '/home/zh/Downloads/chromedriver'
    position = []

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.url = 'https://www.lagou.com/jobs/list_python?city=%E5%8C%97%E4' \
                   '%BA%AC&cl=false&fromSearch=true&labelWords=&suginput='

    def run(self):
        self.driver.get(self.url)
        while 1:
            source = self.driver.page_source
            WebDriverWait(driver=self.driver, timeout=10).until(
                ec.presence_of_element_located((By.XPATH, "//span[@action='next']"))
                )
            self.list_page(source)
            next_button = self.driver.find_element_by_class_name('pager_next ')

            if "pager_next_disabled" in next_button.get_attribute('class'):
                break
            else:
                next_button.click()
            print('*'*30)

    def list_page(self, source):
        html = etree.HTML(source)
        urls = html.xpath("//a[@class='position_link']/@href")
        for url in urls:
            self.get_detail(url)

    def get_detail(self, url):
        # self.driver.get(url)
        self.driver.execute_script("window.open('%s')" % url)
        self.driver.switch_to_window(self.driver.window_handles[1])
        WebDriverWait(driver=self.driver, timeout=10).until(
            ec.presence_of_element_located((By.XPATH, "//span[@class='name']"))
        )
        source = self.driver.page_source
        self.parse_detail(source)
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])

    def parse_detail(self, source):
        html = etree.HTML(source)
        position_name = html.xpath('//span[@class="name"]/text()')[0]
        company = html.xpath('//div[@class="company"]/text()')[0]
        body = html.xpath('//p/span/text()')
        salary = body[0]
        work_place = re.sub(r'[\s/]', '', body[1]).strip()
        work_experience = re.sub(r'\s/', '', body[2]).strip()
        education = re.sub(r'\s/', '', body[3]).strip()
        style = re.sub(r'\s/', '', body[4]).strip()
        work_detail = "".join(html.xpath("//div[@class='job-detail']/p/text()")).strip()
        position = {
            'name': position_name,
            'company': company,
            'salary': salary,
            'place': work_place,
            'experience': work_experience,
            'education': education,
            'style': style,
            'request': work_detail
        }
        self.position.append(position)
        print('^'*30)
        with open('position_info', 'w', encoding='utf-8') as fp:
            json.dump(self.position, fp, ensure_ascii=False)


if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()

