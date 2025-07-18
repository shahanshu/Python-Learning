import requests

def fetch(url, path):
    r = requests.get(url)
    with open(path, 'w', encoding='utf-8') as file:
        file.write(r.text)

url = "https://www.hamropatro.com/news"
fetch(url, "data.html")
