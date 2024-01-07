import json
import requests as req
url = "https://www.4gamers.com.tw/site/api/news/by-tag?tag=%E9%99%90%E6%99%82%E5%85%8D%E8%B2%BB&nextStart=0&pageSize=25"
res = req.get(url)
data = json.loads(res.text)
urlPush = data["data"]["results"][0]["canonicalUrl"]
print(urlPush)
