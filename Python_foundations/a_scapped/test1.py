import requests
from bs4 import BeautifulSoup

with open('sample.html','r') as f:
    reading=f.read()


soup =BeautifulSoup(reading,'html.parser')
soup.prettify()

print(soup.tittle)