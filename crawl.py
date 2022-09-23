from bs4 import BeautifulSoup
import requests


def get_HUST_notice():
    r = requests.get("https://www.hust.edu.cn/tzgg.htm")
    html = r.content.decode()
    # lxml解析
    soup = BeautifulSoup(html, "lxml")
    # 通知放在"wp_news_w7"里
    news = soup.find(id="wp_news_w7")
    # 寻找a标签
    items = news.findAll("a")
    res = {}
    for i in items:
        title = i["alt"]
        href = i["href"]
        res[title] = href
    return res


def get_CSE_notices():
    r = requests.get("http://cse.hust.edu.cn/index/tzgg.htm")
    html = r.content.decode()
    # lxml解析
    soup = BeautifulSoup(html, "lxml")
    body = soup.find(id="content")
    news = body.findAll("a")
    # print(news)
    res = {}
    for i in news:
        if i.text == '2':
            break
        title = i["title"]
        href = str(i["href"])
        if href[0] == ".":
            href = href.replace("..", "http://cse.hust.edu.cn/")
        res[title] = href
    return res
