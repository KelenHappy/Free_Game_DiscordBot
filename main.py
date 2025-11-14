import discord
import os
import asyncio
from getUrl import getUrl

try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

url = "https://www.4gamers.com.tw/site/api/news/of-category/1118?nextStart=0&pageSize=25"

bot = discord.Bot(intents=discord.Intents.all())

async def job():
    try:
        print("Executing the code")
        loop = asyncio.get_event_loop()
        url_of_stack = await loop.run_in_executor(None, getUrl, url)
        
        if url_of_stack:
            channel_id = 111111111111111111111111  
            channel = bot.get_channel(channel_id)
            if channel:
                for url_temp in url_of_stack:
                    message = f"New URL found: {url_temp}"
                    await channel.send(message)
                    print(url_temp)
        else:
            print("No new URLs were detected.")
        
        print("Job completed.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await bot.close()

@bot.event
async def on_ready():
    print(f"「{bot.user}」has logged in")
    await job()

async def main():
    await bot.start(os.getenv("BOT_TOKEN"))

if __name__ == "__main__":
    asyncio.run(main())
