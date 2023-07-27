import requests
import json
import re
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

def processing_data2(data_str: str):
    data_str = data_str.replace("\n", "").replace("\t", "")

    while "  " in data_str:
        data_str = data_str.replace("  ", " ")

    find_key = re.compile("(.*?):.*?")
    keys = re.findall(find_key, data_str)
    keys = list(set(keys))

    for k in keys:
        print(k)
        data_str = data_str.replace(k.strip(), f"\"{k.strip()}\"")

    return data_str


def processing_data(data_str: str):
    find = {"name:": 1, "classification:": 1, "issues:": 1, "description:": 1, "noflip:": 1, "notitle:": 1,
            "data:": 1}
    for k in find:
        if k in data_str:
            data_str = data_str.replace(f"{k}", f"\"{k}\":")

    while "  " in data_str:
        data_str = data_str.replace("  ", " ")

    data_str = data_str.replace("\n", "")\
        .replace("\t", "")\
        .replace("},]", "}]")\
        .replace(" \"issues\" ", "'issues'")

    return data_str


def data_from_msci():
    # url = "https://www.msci.com/our-solutions/esg-investing/esg-industry-materiality-map"
    #
    # resp = requests.get(url=url, headers=headers)
    with open("msci.html", "r") as file:
        resp = file.read()
    # html = BeautifulSoup(resp.text, "html.parser")
    html = BeautifulSoup(resp, "html.parser")

    # find_themes = re.compile(r"<script>.*?var themes = (.*?);.*?//GICS code: data array", re.S)
    find_data = re.compile(r"<script>.*?var themes = (.*?);.*?//GICS code: data array.*?"
                                  r"var sectorData =(.*?);.*?var subsectorData =(.*?);.*?"
                                  r"var coverage =(.*?)", re.S)

    data = re.findall(find_data, str(html))[0]
    for d in data:
        d = processing_data2(d.strip())
        print(d)
        _json = json.loads(d)
        print(_json)
    print(len(data))

    # themes_str = processing_data(re.findall(find_themes, str(html))[0].strip())
    # theme = json.loads(themes_str)

    # sector_data_str = re.findall(find_themes, str(html))
    # print(sector_data_str)

    # with open("data/raw/raw_theme.json", "w") as file:
    #     file.write(json.dumps(theme))


def reformulate_theme_data():
    with open("data/raw/raw_theme.json", "r") as file:
        theme = json.loads(file.read())

    theme_by = {"environment": {}, "social": {}, "governance": {}}

    for t in theme:
        issues = []
        for i in t["issues"]:
            issues.append(i["name"])
        theme_by[t["classification"].lower()][t["name"]] = issues

    with open("data/reformulate/reformulate_theme.json", "w") as file:
        file.write(json.dumps(theme_by))


if __name__ == '__main__':
    data_from_msci()
