import discord
import os
from getUrl import getUrl
import asyncio

url = "https://www.4gamers.com.tw/site/api/news/by-tag?tag=%E9%99%90%E6%99%82%E5%85%8D%E8%B2%BB&nextStart=0&pageSize=25"

bot = discord.Bot(intents=discord.Intents.all())

async def job():
    try:
        print("Executing the code")
        url_of_stack = getUrl(url)
        if url_of_stack:
            channel_id = 111111111111111111111111  # Replace with your actual channel ID
            channel = bot.get_channel(channel_id)
            if channel:
                for url_temp in url_of_stack:
                    message = f"New URL found: {url_temp}"
                    await channel.send(message)
        print("Job completed.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await bot.close()

@bot.event
async def on_ready():
    print(f"「{bot.user}」已登入")
    await job()

# Run the bot asynchronously
async def main():
    await bot.start(os.getenv("BOT_TOKEN"))

asyncio.run(main())
