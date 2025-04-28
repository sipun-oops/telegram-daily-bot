import asyncio
from telegram import *
import schedule
import time

BOT_TOKEN = "7796728205:AAHxPoT8hWWEK_GA_Wn9zG-O4oez0qgWlRY"
CHAT_ID = "@vapourwavechannel"

bot = Bot(token = BOT_TOKEN)

async def daily_post():
    text = "🌞 Good morning! Here’s your daily motivation:\n\n✨ 'Keep pushing forward!'"
    await bot.send_message(chat_id=CHAT_ID, text=text)
    print("message send")
    

def schedule_job():
    asyncio.run(daily_post())

schedule.every().day.at("07:26").do(schedule_job)


while True:
    schedule.run_pending()
    time.sleep(30)
