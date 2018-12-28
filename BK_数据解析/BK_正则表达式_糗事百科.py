import requests
import re,json,csv

Headers = {
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
}


def main():
    url = 'https://www.qiushibaike.com/text/page/{}/'
    headers = ['段子']
    for x in range(1,10):
        urls = url.format(x)
        a = parser_page(urls)
        print(a)
    # with open('糗事百科.json', 'w', encoding='utf-8')as fp:
    #     json.dump(a, fp, ensure_ascii=False)
    # with open('糗事百科.csv', 'w', encoding='utf-8')as fp:
    #     writer = csv.DictWriter(fp, headers)
    #     writer.writeheader()
    #     writer.writerows(a)


def parser_page(url):
    resp = requests.get(url, headers=Headers)
    text = resp.content.decode('utf-8')
    contents = re.findall(r'<div class="content">.*?>(.*?)</span>', text, re.DOTALL)
    duanzi = []
    # xiaohua = {}
    for content in contents:
        x = re.sub('<br/>', '', content).strip()
        # xiaohua['段子'] = x
        duanzi.append(x)
    return duanzi


if __name__ == '__main__':
    main()
