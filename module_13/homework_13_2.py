import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage


load_dotenv("/usr//local/.env")

bot = Bot(os.getenv("API_Ub"))
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text=['Urban', 'ff'])
async def urban_message(message):
    print('Urban message')
    await message.answer('Принято')


@dp.message_handler(commands=['start'])
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Добро пожаловать')


@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer(f'Сам такой {message.text}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
