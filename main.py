import discord
import os
from getUrl import getUrl
from keep_alive import keep_alive
import asyncio
from datetime import datetime, timedelta

TIME_FILE_PATH = "time.txt"
url = "https://www.4gamers.com.tw/site/api/news/by-tag?tag=%E9%99%90%E6%99%82%E5%85%8D%E8%B2%BB&nextStart=0&pageSize=25"

bot = discord.Bot(intents=discord.Intents.all())

def read_last_execution_time():
    try:
        with open(TIME_FILE_PATH, 'r') as file:
            content = file.read().strip()
            if content:
                return float(content)
            else:
                return 0
    except FileNotFoundError:
        return 0

def write_last_execution_time(timestamp):
    with open(TIME_FILE_PATH, 'w') as file:
        file.write(str(timestamp))

async def job():
    print("Executing the code every day at 12:00 and 24:00")
    getUrl(url)
    current_time = time.time()
    write_last_execution_time(current_time)

async def run_jobs():
    while True:
        await asyncio.sleep(1)
        schedule.run_pending()

@bot.event
async def on_ready():
    print(f"「{bot.user}」已登入")

async def main():
    # Read the last execution time from the file
    last_execution_time = read_last_execution_time()

    # Calculate the next scheduled execution times at 12:00 and 24:00
    next_execution_time_12 = datetime.fromtimestamp(last_execution_time) + timedelta(hours=24)
    next_execution_time_24 = datetime.fromtimestamp(last_execution_time) + timedelta(hours=12)

    # Schedule the job to run at 12:00 and 24:00
    schedule.every().day.at(next_execution_time_12.strftime("12:00")).do(job)
    schedule.every().day.at(next_execution_time_24.strftime("00:00")).do(job)

    # Run the scheduled jobs in a loop
    await asyncio.gather(run_jobs(), bot.start(os.environ['bot_token']))

# Run the main asynchronous function
asyncio.run(main())
