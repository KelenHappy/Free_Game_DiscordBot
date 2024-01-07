import discord
import os
from getUrl import getUrl
from keep_alive import keep_alive
import asyncio
import aioschedule
import time
from datetime import datetime, timedelta

TIME_FILE_PATH = "time.txt"
url = "https://www.4gamers.com.tw/site/api/news/by-tag?tag=%E9%99%90%E6%99%82%E5%85%8D%E8%B2%BB&nextStart=0&pageSize=25"

bot = discord.Bot(intents=discord.Intents.all())

def read_last_execution_time():
    try:
        with open(TIME_FILE_PATH, 'r') as file:
            content = file.read().strip()
            if content and content.replace(".", "", 1).isdigit():
                return float(content)
            else:
                return 0
    except FileNotFoundError:
        return 0

def write_last_execution_time(timestamp):
    with open(TIME_FILE_PATH, 'w') as file:
        file.write(str(timestamp))

async def job():
    try:
        print("Executing the code every 5 minutes")
        url_of_stack = getUrl(url)
        if url_of_stack:
            #change this
            channel_id = 123456789123456  # Replace with your actual channel ID
            channel = bot.get_channel(channel_id)

            if channel:
                for url_temp in url_of_stack:
                    message = f"New URL found: {url_temp}"
                    await channel.send(message)

        current_time = time.time()
        write_last_execution_time(current_time)

    except Exception as e:
        print(f"An error occurred: {e}")



async def run_jobs():
    while True:
        await asyncio.sleep(1)
        await aioschedule.run_pending()

@bot.event
async def on_ready():
    print(f"「{bot.user}」已登入")

async def main():
    # Read the last execution time from the file
    last_execution_time = read_last_execution_time()

    # Calculate the next scheduled execution time 5 minutes from now
    next_execution_time = datetime.fromtimestamp(last_execution_time) + timedelta(minutes=5)

    # Schedule the job to run every 5 minutes
    aioschedule.every(5).minutes.do(job)

    # Run the scheduled jobs in a loop
    await asyncio.gather(run_jobs(), bot.start(os.environ['bot_token']))

# Run the main asynchronous function
asyncio.run(main())
