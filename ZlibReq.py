import requests
import time

url = "https://zh.zlib-domains.sk/"
headers = {
    "Authorization": "aMaaSIA86Uq8mOzt", # 暂时不知道这个是什么, 有可能是版本号的hash
    "source": "android",
}

output_file = f'./results/{time.strftime("%Y-%m-%d-%H-%M-%S")}.txt'
with open(output_file, 'w') as f:
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
                f.write(f"error: {e}\n")
                return False
                
        data = response.json()
        for datai in data:
            domain = datai["domain"]
            contentAvailable = datai["contentAvailable"]
            print(f"domain: {domain}, contentAvailable: {contentAvailable}")
            f.write(f"domain: {domain}, contentAvailable: {contentAvailable}\n")
            ok200 = get_avilability(domain)
            print(f"ok200: {ok200}")
            f.write(f"ok200: {ok200}\n")
            
    except Exception as e:
        print(e)
        f.write(f"error: {e}\n")