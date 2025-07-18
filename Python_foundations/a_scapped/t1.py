import requests



proxies={


        "http": "http://sprwozfe:fk2epjvp3n3b@38.154.227.167:5868/",
        "https": "http://sprwozfe:fk2epjvp3n3b@38.154.227.167:5868/"
    }

r=requests.get(url="https://api.ipify.org", proxies=proxies)
print(r.text)