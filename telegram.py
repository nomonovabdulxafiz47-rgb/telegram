import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart

# Bot tokeningizni shu yerga yozing
TOKEN = "9140076102:AAHuSIGr7B9c1YEzg5PBQn06A4eXM4p7UHI

# Dispatcher va Bot obyektini yaratish
dp = Dispatcher()

# /start komisskasi uchun handler
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Assalomu alaykum! Menga 'salom' deb yozib ko'ring.")

# 'salom' so'ziga javob beruvchi handler (katta-kichik harflarga e'tibor bermasligi uchun .lower() ishlatamiz)
@dp.message(F.text.lower() == "salom")
async def send_welcome(message: Message):
    await message.answer("Salom! Qalaysiz?")

async def main():
    bot = Bot(token=TOKEN)
    # Botni ishga tushirish
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
