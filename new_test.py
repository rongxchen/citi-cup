import requests

url = 'http://globalesg.xignite.com/xGlobalESG.json/GetESGCategories?IdentifierType=Symbol&Identifiers=AAPL, AZN.XLON&IdentifierAsOfDate=7/26/2023&AsOfDate=7/26/2023&_token=USER_TOKEN'

response = requests.get(url)
print(response.text)
