# ВВеди в терминал pip install aiogram==2.25.1 - поставь интерпритатор 3.10

import logging
# import os.path

from aiogram import types    #, Bot, Dispatcher
from aiogram.utils import executor
# import os
from Buttons import start
# from aiogram.types import InputFile           # не всегда
from config import bot, dp, admin
from handlers import commands, echo, quiz


# TOKEN = '7284812005:AAGnVo_DzjVsxrO0m2L2dX2XcsY0PiH0dGo'
#
# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot=bot)
#
# admin = [799303538, ]

async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text="Бот включен!", reply_markup=start)     # глушится нижним

commands.register_commands(dp)
# quiz.register_quiz(dp)



echo.register_echo(dp)
# commands.register_commands(dp)

# @dp.message_handler(commands=['start'])
# async def start_handler(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id, text ='Hello!', reply_markup=start_test)     # добавляй чтобы добавить кнопку но просто старт, если старстест то он глушит первую кнопку
#     # await message.answer(text='Привет!')




# @dp.message_handler(commands=['mem'])
# async def mem_handler(message: types.Message):
#     folder = 'media'
#
#     photo_path = os.path.join(folder, 'img.png')
#
#     with open(photo_path, 'rb') as photo:              # два вида open открывает и не закрывает, with open и то и другое
#         await message.answer_photo(photo=photo)            # rb - прочитать в бинарном режиме
#
# @dp.message_handler(commands=['mem_all'])
# async def mem_all_handler(message: types.Message):
#     folder = 'media'
#     photos = os.listdir(folder)       # если все картинки вытащить
#
#     for photo_name in photos:
#         photo_path = os.path.join(folder, photo_name)
#
#         if photo_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
#             with open(photo_path, 'rb') as photo:
#                 await bot.send_photo(chat_id=message.from_user.id, photo=photo)
#                 # await bot.send_photo(message.from_user.id, photo)     # можно так тоже бот понимает
#
#
#
# @dp.message_handler(commands=['music'])
# async def music_handler(message: types.Message):
#     folder = 'audio'
#     music_name = "track.mp3"
#
#     music_path = os.path.join(folder, music_name)
#
#     with open(music_path, 'rb') as music:
#         # await message.answer_audio(InputFile(music))           # вариант
#         await message.answer_audio(music)


#
# @dp.message_handler()
# async def echo_handler(message: types.Message):
#     await message.answer(message.text)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

# В терминале пиши: python main.py
# в терминале чтобы остановить бот - crtl c