from ssl import CHANNEL_BINDING_TYPES
import discord
import os
import asyncio
from getUrl import getUrl

url = "https://www.4gamers.com.tw/site/api/news/of-category/1118?nextStart=0&pageSize=25"
# Replace with your actual channel ID
CHANNEL_ID = 111111111111111111111111 

async def job(bot):
    try:
        print("Executing the code")
        loop = asyncio.get_event_loop()
        url_of_stack = await loop.run_in_executor(None, getUrl, url)
        
        if url_of_stack:
            channel = bot.get_channel(CHANNEL_ID)
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

async def main():
    # Create a bot
    intents = discord.Intents.default()
    intents.message_content = True
    bot = discord.Bot(intents=intents)

    @bot.event
    async def on_ready():
        print(f"「{bot.user}」has logged in")
        await job(bot)  # Execute job once the bot is ready

    # Get Bot Token
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("BOT_TOKEN environment variable not set.")
        return
    
    try:
        await bot.start(token)
    except Exception as e:
        print(f"Failed to start bot: {e}")
    

if __name__ == "__main__":
    asyncio.run(main())
