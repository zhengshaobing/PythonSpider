import requests
import re,csv,json


'''
爬取中国古诗词网
'''
Headers = {
'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
'referer':'https://www.gushiwen.org/default_2.aspx'
}

b =[]
def main():
    base_url = 'https://www.gushiwen.org/default_{}.aspx'
    headers = ["作者", "朝代", "题目", "内容"]
    for x in range(1, 10):
        urls = base_url.format(x)

        a = parse_page(urls)
        b.extend(a)
        print('*'*30)
    # print(b)
       # 写作json文件
    with open('古诗词.json', 'w', encoding='utf-8')as fp:
        json.dump(b, fp, ensure_ascii=False)
    with open('古诗词.csv', 'w', encoding='utf-8')as fp:
        writer = csv.DictWriter(fp, headers)
        writer.writeheader()
        writer.writerows(b)


def parse_page(url):
    resp = requests.get(url,headers=Headers)
    text = resp.content.decode('utf-8')
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>', text, re.DOTALL)
    dynasty = re.findall(r'<p\sclass="source">.*?<a.*?>(.*?)</a>.*?<a.*?>.*?</a>.*?</p>', text, re.DOTALL)
    authors = re.findall(r'<p\sclass="source">.*?<a.*?>.*?</a>.*?<a.*?>(.*?)</a>.*?</p>', text, re.DOTALL)
    poetry = re.findall(r'<div\sclass="contson".*?>(.*?)</div>', text, re.DOTALL)
    contens = []
    for x in poetry:
        poetries = re.sub(r'<br />', '' ,x).strip()
        contens.append(poetries)
    poems = []
    for value in zip(titles,dynasty,authors,contens):
        title,dynasty,author,conten = value
        poem = {
            '题目': title,
            '朝代': dynasty,
            "作者": author,
            '内容': conten
        }
        poems.append(poem)
    return (poems)


if __name__ == '__main__':
    main()