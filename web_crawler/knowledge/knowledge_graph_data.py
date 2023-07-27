import requests
import zhconv.zhconv


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

def fetch(entity):
    entity = zhconv.convert(entity, "zh-cn")
    print(entity)

    url = f"https://api.ownthink.com/kg/knowledge?entity={entity}"
    resp = requests.get(url=url)

    data = resp.json()["data"]

    if data == "":
        return []

    avp = data["avp"]

    nodes = []

    for ap in avp:
        if ap[1] == data["entity"]:
            continue
        nodes.append({"source": data["entity"], "target": ap[1], "rela": ap[0], "type": "resolved"})

    return nodes