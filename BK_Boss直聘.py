import re,json
from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class BossSpider(object):
    driver_path = '/home/zh/Downloads/chromedriver'
    base_url = 'https://www.zhipin.com'
    job = []

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.url = 'https://www.zhipin.com/c100010000/?query=python&page=1&ka=page-1'

    def run(self):
        self.driver.get(self.url)
        while 1:
            source = self.driver.page_source
            WebDriverWait(driver=self.driver, timeout=10).until(
                ec.presence_of_element_located((By.XPATH, '//a[@class="next"]'))
            )
            self.list_page(source)
            next_button = self.driver.find_element_by_class_name("next")
            if 'next disabled' in next_button.get_attribute('class'):
                break
            else:
                next_button.click()
                print("*"*50)

    def list_page(self, source):
        html = etree.HTML(source)
        urls = html.xpath('//div[@class="info-primary"]//a/@href')
        for url in urls:
            url = self.base_url + url
            self.get_detail(url)

    def get_detail(self, url):
        self.driver.execute_script("window.open('%s')" % url)
        self.driver.switch_to_window(self.driver.window_handles[1])
        source = self.driver.page_source
        self.parse_page(source)
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])

    def parse_page(self, source):
        html = etree.HTML(source)
        name = html.xpath('//div[@class="name"]/h1/text()')[0]
        salary = html.xpath('//span[@class="badge"]/text()')[0].strip()
        request = html.xpath('//*[@id="main"]/div[1]/div/div/div[2]/p/text()')
        city = request[0]
        experience = request[1]
        education = request[2]
        company = html.xpath('//*[@id="main"]/div[1]/div/div/div[3]/h3/a/text()')[0]
        job_describe = "".join(html.xpath('//*[@id="main"]/div[3]/div/div[2]/div[3]/div[1]/div/text()')).strip()
        info = {
            '职位': name,
            '薪水': salary,
            '城市': city,
            '经验': experience,
            '学历': education,
            '公司': company,
            '职位信息':job_describe
        }
        self.job.append(info)
        # with open("python职位.json", 'w', encoding='utf-8') as fp:
        #     json.dump(self.job, fp)


if __name__ == '__main__':
    spider = BossSpider()
    spider.run()