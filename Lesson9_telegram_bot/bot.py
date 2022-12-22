import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import interface
import data_file
from datetime import datetime

#При вводе будет необходимо запросить 4 значения счётчиков
meters_count = -1
meter_list = [0] * 4

load_dotenv()
TOKEN = os.getenv("TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.answer(text= "Привет! Это бот для ввода показаний счётчиков.\nВыберите пункт меню:",
                         reply_markup=interface.MAIN_MENU)
    #await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")



@dp.message_handler()
async def echo(message: types.Message):
    global meters_count
    if meters_count >= 0:
        if meters_count == 0:
            meter_list[meters_count] = message.text.replace(" ", "")
            await message.answer(text= "Введите Санузел. Холодная вода")
            meters_count+=1
        elif meters_count == 1:
            meter_list[meters_count] = message.text.replace(" ", "")
            await message.answer(text= "Введите Кухня. Горячая вода")
            meters_count+=1    
        elif meters_count == 2:
            meter_list[meters_count] = message.text.replace(" ", "")
            await message.answer(text= "Введите Кухня. Холодная вода")
            meters_count+=1    
        elif meters_count == 3:
            meter_list[meters_count] = message.text.replace(" ", "")
            await message.answer(text= "Показания приняты",
                                 reply_markup=interface.MAIN_MENU)
            meters_count = -1    
            data_file.save_to_file(meter_list)
        
        print(meter_list[meters_count])
        print(meters_count)    
    else:        
        await message.answer(text= "Введите команду /start или выберите из пункта меню")


@dp.callback_query_handler(text='get_last')
async def process_callback_get_last(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message( callback_query.from_user.id,
                            text= data_file.get_last_data(),
                            reply_markup=interface.MAIN_MENU)


@dp.callback_query_handler(text='get_current')
async def process_callback_get_current(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id) 
    text = data_file.get_current_data()
    if text == False: text = "За текущий месяц показания не вводили"   
    await bot.send_message( callback_query.from_user.id,
                            text= text,
                            reply_markup=interface.MAIN_MENU)
                       

@dp.callback_query_handler(text='input_meters')
async def process_callback_input_meters(callback_query: types.CallbackQuery):
    global meters_count
    await bot.answer_callback_query(callback_query.id)
    meters_count = 0
    await bot.send_message(callback_query.from_user.id,
                           text= "Введите Санузел. Горячая вода")
   
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)