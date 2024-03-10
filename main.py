import discord
import os
import asyncio  # 添加這一行
from getUrl import getUrl

url = "https://www.4gamers.com.tw/site/api/news/by-tag?tag=%E9%99%90%E6%99%82%E5%85%8D%E8%B2%BB&nextStart=0&pageSize=25"

bot = discord.Bot(intents=discord.Intents.all())

async def job():
    try:
        print("Executing the code")
        url_of_stack = getUrl(url)
        if url_of_stack:
            #change this
            channel_id = 123456789123456  # Replace with your actual channel ID
            channel = bot.get_channel(channel_id)

            if channel:
                for url_temp in url_of_stack:
                    message = f"New URL found: {url_temp}"
                    await channel.send(message)

        # Here we can exit the bot after executing the job
        await bot.close()

    except Exception as e:
        print(f"An error occurred: {e}")

@bot.event
async def on_ready():
    print(f"「{bot.user}」已登入")

def main():
    # Run the job
    asyncio.run(job())

# Run the main synchronous function
main()
