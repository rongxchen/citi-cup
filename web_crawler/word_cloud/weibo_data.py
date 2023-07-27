import requests
import jieba
import re
import os
from wordcloud import WordCloud
from urllib.parse import quote

from web_crawler.utils import get_random_ua, get_random_proxy


def processing_text(text: str):
    text = re.sub(r"<span.*?>.*?</span>", "", text)
    text = re.sub(r"<img.*?>.*?</img>", "", text)
    text = re.sub(r"<a.*?>.*?</a>", "", text)
    text = re.sub(r"<h.*?>.*?</h.>", "", text)
    text = re.sub(r'[;<>"~!@#$%^&*()|{}/.,?【】～，。“”；？！（）]', "", text)
    return text


def find_card_type_9(card: dict):
    if card["card_type"] != 9:
        for _card in card["card_group"]:
            if _card["card_type"] == 9:
                return processing_text(_card["mblog"]["text"])
    return ""


def blogs_from_weibo(keyword: str, pages: int = 10):
    try:
        data = []
        for i in range(1, pages+1):
            quoted = "containerid=100103type" + quote(f"=1&q={keyword}")
            url = f"https://m.weibo.cn/api/container/getIndex?{quoted}&page_type=searchall&page={i}"
            resp = requests.get(url=url, headers={"user-agent": get_random_ua()}, proxies=get_random_proxy())
            data.extend(resp.json()["data"]["cards"])
        words = ""
        for d in data:
            words += find_card_type_9(d)
        print(words)
        word_cloud_generator(keyword, words)
    except Exception as e:
        print(f"exception: {e}")


def word_cloud_generator(company: str, words: str):
    word_list = jieba.cut(words, cut_all=True)
    word_list = list(set(word_list))
    new_words = " ".join(word_list)
    word_cloud = WordCloud(
        font_path=r"C:\Users\chenr\PycharmProjects\Citi\web_crawler\word_cloud\逐浪雅宋体.otf",
        background_color="white",
    ).generate(new_words)
    word_cloud.to_file(f"C:\\Users\\chenr\\PycharmProjects\\Citi\\web_crawler\\word_cloud\\img\\{company}.jpg")
    print("word cloud saved")

    with open(f"C:\\Users\\chenr\\PycharmProjects\\Citi\\web_crawler\\word_cloud\\img\\{company}.jpg", "rb") as file:
        binary_data = file.read()

    with open("C:\\Users\\chenr\\PycharmProjects\\Citi\\static\\images\\wordcloud\\" + company + ".jpg", "wb") as file:
        file.write(binary_data)
        print(file.name)
        print("write image success")


def return_image_location(company: str):
    # path = "C:\\Users\\chenr\\PycharmProjects\\Citi\\static\\images\\wordcloud\\" + company + ".jpg"
    # if not os.path.exists(path):
    blogs_from_weibo(company)
    return f"../../../static/images/wordcloud/{company}.jpg"
