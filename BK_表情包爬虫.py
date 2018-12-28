import requests
from lxml import etree
import csv,os,re,threading
from urllib import request
from queue import Queue
'''
传统模式下爬取网络图片
'''


# def parse_page(url):
#     headers = {
#         'Referer':'https: // www.doutula.com / photo / list /?page = 1',
#         'User-Agent':'Mozilla / 5.0(X11;Linuxx86_64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 71.0.3578.80Safari / 537.36'
#     }
#     resp = requests.get(url, headers=headers)
#     text = resp.content.decode('utf-8')
#     html = etree.HTML(text)
#     pictures = html.xpath('//div[@class="page-content text-center"]//img[@class!="gif"]')
#     for picture in pictures:
#         img_url = picture.get('data-original')
#         alt = picture.get('alt')
#         alt = re.sub(r'[\?？\.。\,，\!]', '', alt)
#         suffix = os.path.splitext(img_url)[1]
#         file_name = alt+suffix
#         request.urlretrieve(img_url, 'images/'+file_name)
#
#
# def page_control():
#     base_url = 'https://www.doutula.com/photo/list/?page={}'
#     for x in range(1, 101):
#         urls = base_url.format(x)
#         parse_page(urls)
#         break
#

# def main():
#     page_control()
#
#
# if __name__ == '__main__':
#    main()

'''
多线程爬虫，使用queen队列来实现
'''
# class Producer(threading.Thread):
#     headers = {
#         'Referer': 'https: // www.doutula.com / photo / list /?page = 1',
#         'User-Agent': 'Mozilla / 5.0(X11;Linuxx86_64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 71.0.3578.80Safari / 537.36'
#     }
#
#     def __init__(self, page_queen, image_queen, *args, **kwargs):
#         super(Producer, self).__init__(*args, **kwargs)
#         self.page_queen = page_queen
#         self.image_queen = image_queen
#
#     def run(self):
#         while 1:
#             if self.page_queen.empty():
#                 break
#             url = self.page_queen.get()
#
#             self.parse_page(url)
#
#     def parse_page(self, url):
#         resp = requests.get(url, headers=self.headers)
#         text = resp.text
#         html = etree.HTML(text)
#         pictures = html.xpath('//div[@class="page-content text-center"]//img[@class!="gif"]')
#         for picture in pictures:
#             img_url = picture.get('data-original')
#             alt = picture.get('alt')
#             alt = re.sub(r'[\?？\.。\,，\!\*]', '', alt)
#             suffix = os.path.splitext(img_url)[1]
#             filename = alt+suffix
#             print(filename)
#             self.image_queen.put((img_url, filename))
#
#
# class Consumer(threading.Thread):
#     def __init__(self, page_queen, image_queen, *args, **kwargs):
#         super(Consumer, self).__init__(*args, **kwargs)
#         self.page_queen = page_queen
#         self.image_queen = image_queen
#
#     def run(self):
#         while True:
#             # if self.image_queen.empty() and self.page_queen.empty():
#             #     break
#             img_url, filename = self.image_queen.get()
#             print(img_url)
#             # request.urlretrieve(img_url, 'images/'+filename)
#
#             if self.image_queen.empty() and self.page_queen.empty():
#                 break
#             print('*'*30)
#
#
# def page_control():
#     image_queen = Queue(300)
#     page_queen = Queue(10)
#     base_url = 'https://www.doutula.com/photo/list/?page={}'
#     for x in range(1, 10):
#         urls = base_url.format(x)
#         page_queen.put(urls)
#     for x in range(5):
#         t = Producer(page_queen, image_queen)
#         t.start()
#     for x in range(5):
#         t = Consumer(page_queen, image_queen)
#         t.start()
#
#
# def main():
#     page_control()
#
#
# if __name__ == '__main__':
#     main()
