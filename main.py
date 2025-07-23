import discord
import os
import asyncio
from getUrl import getUrl

url = "https://www.4gamers.com.tw/site/api/news/of-category/1118?nextStart=0&pageSize=25"

bot = discord.Bot(intents=discord.Intents.all())

async def job():
    try:
        print("Executing the code")
        # If getUrl is synchronous, use run_in_executor
        loop = asyncio.get_event_loop()
        url_of_stack = await loop.run_in_executor(None, getUrl, url)
        
        if url_of_stack:
            # Replace with your actual channel ID
            # 更換你的頻道ID
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
        await bot.close()  # Close the bot

@bot.event
async def on_ready():
    print(f"「{bot.user}」has logged in")
    await job()  # Execute job once the bot is ready

# Run the bot
async def main():
    await bot.start(os.getenv("BOT_TOKEN"))

if __name__ == "__main__":
    asyncio.run(main())
