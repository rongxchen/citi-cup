import requests
import json

from web_crawler.chatgpt.FinBERT import *


api_key = ""

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

message_template = """I will give you a link of news article, help me to analyze:
1) the news sentiment (i.e., Positive / Neutral / Negative); 
2) ESG category (i.e., Environment, Social, Governance, or all the above (ESG)); 
3) a few sentences to summarize the article;
4) entities involved;
5) company name (if any);
6) stock code (if any);
7) industry (if any);
Please return your answers in form of json, i.e., {"sentiment": sentiment, "category": category, "entities": entities, "name": companyName, "code": stockCode, "industry": industry, "summary": summary}.
Here is the link: """

"""
entity
name
stock code
industry
"""

url = "https://api.openai.com/v1/chat/completions"

def chat(link: str):
    message = message_template + link

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": message}],
        "max_tokens": 3560,
        "temperature": 0.7
    }

    resp = requests.post(url=url, headers=headers, data=json.dumps(data))

    print(resp.json())

    try:
        reply = resp.json()["choices"][0]["message"]["content"].strip().replace("\n", "")
        json_data = json.loads(reply)
        json_data["link"] = link
        print(json_data)

        text = json_data["summary"]
        senti = FinBERT_sentiment(text)[0]
        print(senti)
        json_data["sentiment"] = f"{senti['label']} ({round(senti['score'], 2)})"
        esg = FinBERT_ESG(text)[0]
        print(esg)
        json_data["category"] = f"{esg['label']} ({round(esg['score'], 2)})"

        return json_data
    except Exception as e:
        print(f"error occurred: {e}")

    return "error"


def chat_other(description: str, prompt: str = ""):
    # prompt = "I will give you a description in chinese (which is regarding the ESG financing use of a company), " \
    #          "can you identify the recommended financing product " \
    #          "(including 1. green bond; 2. social responsibility bond; 3. sustainable bond; 4. sustainable linked bond)?" \
    #          "please return your answer as one of the choices I gave to you in prompt, the answer should in " \
    #          "small letters and ignore any numbers and special characters." \
    #          "the description is: " + description

    prompt = "I will give you a description in chinese (which is regarding the ESG financing use of a company), " \
             "can you identify the recommended financing (1) product " \
             "(including a. green_bond; b. social_responsibility_bond; c. sustainable_bond; d. sustainable_linked_bond)?" \
             "also, I would like to you determine the (2) interest rate (in number, excluding the %) and financing (3) duration " \
             "(in number, excluding the word year) and suggested financing (4) amount (in ￥, but only include the numbers) for me" \
             "please return your answer in a form of json: {\"product\": product, \"rate\": rate, \"duration\": duration}} only." \
             "do not include any Chines in your response, and only in json format which can be parsed directly" \
             "the description is: " + description

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 3560,
        "temperature": 0.7
    }

    resp = requests.post(url=url, headers=headers, data=json.dumps(data))

    print(resp.json())

    try:
        reply = resp.json()["choices"][0]["message"]["content"].strip().replace("\n", "")
        print(reply)
        return json.loads(reply)
    except Exception as e:
        print(f"error occurred: {e}")

    return "error"
