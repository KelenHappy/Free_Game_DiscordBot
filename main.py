from keep_alive import keep_alive
import discord #導入discord
import os

bot = discord.Bot(intents = discord.Intents.all())
#定義物件 intents是前面勾選的三個勾勾

@bot.event
async def on_ready():
    print(f"「{bot.user}」已登入")

keep_alive()
bot.run(os.environ['bot_token']) #運行機器人
import json
import requests as req
url = "https://www.4gamers.com.tw/site/api/news/by-tag?tag=%E9%99%90%E6%99%82%E5%85%8D%E8%B2%BB&nextStart=0&pageSize=25"
res = req.get(url)
data = json.loads(res.text)
urlPush = data["data"]["results"][0]["canonicalUrl"]
print(urlPush)
