import re


# 创建一个字典
hua_zheng_dic = {
    'AAA': 8/8,
    'AA': 7/8,
    'A': 6/8,
    'BBB': 5/8,
    'BB': 4/8,
    'B': 3/8,
    'CCC': 2/8,
    'CC': 1/8,
    'C': 0/8,
}

miao_ying_dic = {
    'AAA':11/11,
    'AA':10/11,
    'A':9/11,
    'BBB':8/11,
    'BB':7/11,
    'B':6/11,
    'CCC':5/11,
    'CC':4/11,
    'C':3/11,
    'DDD':2/11,
    'DD':1/11,
    'D':0/11
}

hua_ce_ITC_dic = {
    'AAA': 9/9,
    'AA': 8/9,
    'A': 7/9,
    'BBB': 6/9,
    'BB': 5/9,
    'B': 4/9,
    'CCC': 3/9,
    'CC': 2/9,
    'C': 1/9,
    'D': 0/9,
}

meng_lang_dic = {
    "AAA":95, 
    "AA":75, 
    "A":65, 
    "BBB":57.5, 
    "BB":52.5, 
    "B":47.5, 
    "CCC": 42.5, 
    "CC":37.5, 
    "C":20
}

zhong_cheng_xin_dic = {
    "AAA":95,
    "AA":75, 
    "A":65, 
    "BBB":57.5, 
    "BB":52.5, 
    "B":47.5, 
    "C": 30
}

zhi_ding_dic = {
    "AAA":95, 
    "AA":75, 
    "A":65, 
    "BBB":57.5, 
    "BB":52.5, 
    "B":47.5, 
    "CCC": 42.5, 
    "CC":37.5, 
    "C":20
}

zhong_cai_dic = {
    "AAA":95,
    "AA":75,
    "A":65,
    "BBB":57.5,
    "BB":52.5,
    "B":47.5,
    "CCC":42.5,
    "CC":37.5,
    "C":20,
}

shang_dao_rong_lu_dic = {
    'A+': 9/9,
    'A': 8/9,
    'A-': 7/9,
    'B+': 6/9,
    'B': 5/9,
    'B-': 4/9,
    'C+': 3/9,
    'C': 2/9,
    'C-': 1/9,
    'D': 0/9,
}

dic = {
    '晨星': lambda x: eval(x)*2/100.0,
    '华证指数': lambda x: hua_zheng_dic[x],
    '妙盈科技': lambda x: miao_ying_dic[x],
    '华测ITC': lambda x: hua_ce_ITC_dic[x],
    '盟浪': lambda x: meng_lang_dic[x]*0.01,
    '中诚信': lambda x: zhong_cheng_xin_dic[x]*0.01,
    '秩鼎': lambda x: zhi_ding_dic[x]*0.01,
    '富时罗素': lambda x: eval(x)/5.0,
    '中财绿经院': lambda x: zhong_cai_dic[x]*0.01,
    '商道融绿': lambda x: shang_dao_rong_lu_dic[x],
}


# 写一个api，利用正则表达式匹配
def match_api(name, x):
    if name == '富时罗素' or name == '晨星':
        return dic[name](re.findall(r'(\d+(?:\.\d+)?)', str(x))[0])
    elif name == '华证指数' or name == '妙盈科技' or name == '华测ITC' or name == '盟浪' or name == '中诚信' or name == '秩鼎' or name == '中财绿经院':
        return dic[name](re.findall(r'[A-Z]+', x)[0])
    elif name == '商道融绿':
        return dic[name](re.findall(r'[A-Z][+-]?', x)[0])
    return None


def comprehensive_esg_rate(esg_rate_list: list):
    score = 0
    count = 0
    for esg_rate in esg_rate_list:
        s = match_api(esg_rate["agency"], esg_rate["score"])
        if not s is None:
            score += float(s)
            count += 1
    obj = {"agency": "综合评分", "score": str(round(score / count * 100, 2)), "level": "", "date": ""}
    print(len(esg_rate_list))
    print(count)
    print(obj)
    return obj


# 测试
# if __name__ == '__main__':
#     print('富时罗素： ', match_api('富时罗素', '4.5'))
#     print('晨星： ', match_api('晨星', '30-40'))
#     print('华证指数： ', match_api('华证指数', 'AAA'))
#     print('妙盈科技： ', match_api('妙盈科技', 'AAA'))
#     print('华测ITC： ', match_api('华测ITC', 'AA'))
#     print('盟浪： ', match_api('盟浪', 'AA'))
#     print('中诚信： ', match_api('中诚信', 'A'))
#     print('秩鼎： ', match_api('秩鼎', 'A'))
#     print('中财绿经院： ', match_api('中财绿经院', 'AAA'))
#     print('商道融绿： ', match_api('商道融绿', 'A+'))
