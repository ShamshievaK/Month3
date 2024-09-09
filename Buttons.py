# Кнопки в боте

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start = ReplyKeyboardMarkup(resize_keyboard=True,    # определяет размер кнопок при false будут не правильные
                            row_width=2)             # сколько кнопок на одной строке
start_buttons = KeyboardButton('/start')
mem_buttons = KeyboardButton('/mem')
mem_all_buttons = KeyboardButton('/mem_all')
music_buttons = KeyboardButton('/music')

start.add(start_buttons, mem_buttons, mem_all_buttons, music_buttons)                   # 1 способ
# после переходи в лессон 1 и импортируй
#======================================================================================================================
# start_test = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(KeyboardButton('/start'))
                                                                       # KeyboardButton('/mem'),
                                                                       # KeyboardButton('/mem_all'),   # закомментировала чтобы сначала кнопка старт потом другой
                                                                       # KeyboardButton('/music'))             # 2 способ