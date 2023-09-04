import logging
import asyncio
import os
import time

from aiogram import Bot, Dispatcher, executor, types

TOKEN = 'token'
chat_id = 0
flag = True

#Configure Logging
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    #That shit is for start or any other command
    await message.reply("Привет!\n\nЭтот бот может уведомлять тебя каждый день о праздниках, которые есть сегодня. Чтобы заставить его работать, пропиши /do_your_job\n\nЧтобы остановить работу бота напиши /stop")
    global chat_id
    chat_id = message.chat.id

#@dp.message_handler(commands=['do_your_job'])
async def holidays():
    while time.localtime().tm_hour != 14 or time.localtime().tm_min != 32 or time.localtime().tm_sec != 0:
        if flag == False:
            return
        await asyncio.sleep(1)  
        print("все еще выполняется")  
    os.system("python -u holidays_script.py")
    fin = open("hlds.txt", "r", encoding="utf-8")
    txt = fin.read()
    await bot.send_message(chat_id, txt) 
    await asyncio.sleep(1)
    await holidays()     

@dp.message_handler(commands=['do_your_job'])
async def holidays_starter(message: types.Message):
    global flag
    flag = True
    await message.reply("Работа бота начата!")
    await holidays()

@dp.message_handler(commands=['stop'])  
async def stop_fun(message: types.Message):
    global flag
    flag = False
    await message.reply("Работа бота остановлена!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
