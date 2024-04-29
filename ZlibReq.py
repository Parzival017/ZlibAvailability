import requests

url = "https://zh.zlib-domains.sk/"
headers = {
    "Authorization": "aMaaSIA86Uq8mOzt", # 暂时不知道这个是什么, 有可能是版本号的hash
    "source": "android",
}

try:
    response = requests.get(url, headers=headers)

    def get_avilability(domain):
        url = f"https://{domain}/eapi/info/ok"
        try:
            response = requests.get(url, headers=headers)
            data = response.json()
            return data["success"] > 0
        except Exception as e:
            print(e)

    data = response.json()
    for datai in data:
        domain = datai["domain"]
        contentAvailable = datai["contentAvailable"]
        print(f"domain: {domain}, contentAvailable: {contentAvailable}")
        ok200 = get_avilability(domain)
        print(f"ok200: {ok200}")
        
except Exception as e:
    print(e)