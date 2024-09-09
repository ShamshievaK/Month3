from aiogram import Bot, Dispatcher
from decouple import config

TOKEN = config('TOKEN')                                        #'7284812005:AAGnVo_DzjVsxrO0m2L2dX2XcsY0PiH0dGo'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

admin = [799303538, ]