import requests
import os

r= requests.get("https://ioepc.vercel.app/api/getbyroll?rollNumber=PUR079BCT008")


print(r.text)