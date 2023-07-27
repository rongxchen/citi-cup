import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

def from_futu(code: str, market: str):
    mkt = "HK" if market == "HKSE" else ("SH" if market == "SSE" else "SZ")
    url = f"https://www.futunn.com/stock/{code}-{mkt}/company-profile"

    required_items = {
        "公司名称": "name",
        "成立日期": "establish_date",
        "会计年结日": "accounting_date",
        "员工数量": "total_employees",
    }

    if mkt == "SH" or mkt == "SZ":
        required_items["A股证券代码"] = "code"
        required_items["法人代表"] = "ceo"
        required_items["公司网址"] = "website"
        required_items["公司简介"] = "business"
    else:
        required_items["公司代码"] = "code"
        required_items["董事长"] = "ceo"
        required_items["网址"] = "website"
        required_items["公司业务"] = "business"

    try:
        resp = requests.get(url=url, headers=headers)
        html = BeautifulSoup(resp.text, "html.parser")

        stock_main = html.select(".company-main")[0]
        company_items = stock_main.select(".company-item")

        company_item_list = {}
        for item in required_items:
            company_item_list[required_items[item]] = {"cn": item, "value": ""}

        for company_item in company_items:
            item_name = company_item.select(".name")[0].text
            item_value = company_item.select(".value")[0].text.replace("\r", "").replace(" ", "")
            if item_name in required_items:
                company_item_list[required_items[item_name]] = {"cn": item_name, "value": str(item_value)}

        return company_item_list

    except Exception as e:
        print(f"exception: {e}")

        temp = {}
        for item in required_items:
            temp[required_items[item]] = {"cn": item, "value": ""}

        return temp