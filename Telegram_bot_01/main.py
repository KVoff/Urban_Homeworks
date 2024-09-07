import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import keyboards
import texts

load_dotenv("/usr//local/.env")


logging.basicConfig(level=logging.INFO)
bot = Bot(os.getenv("API_Ub"))
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer(texts.start, reply_markup=keyboards.start_kb)


@dp.message_handler(text="О нас")
async def about(message):
    await message.answer(texts.about, reply_markup=keyboards.start_kb)


@dp.message_handler(text="Стоимость")
async def price(message):
    await message.answer(text="Что вы хотите купить?",
                         reply_markup=keyboards.catalog_kb)


@dp.callback_query_handler(text="medium")
async def buy_m(call):
    await call.message.answer(texts.Medium_game, reply_markup=keyboards.buy_kb)
    await call.answer()


@dp.callback_query_handler(text="big")
async def buy_b(call):
    await call.message.answer(texts.Large_game, reply_markup=keyboards.buy_kb)
    await call.answer()


@dp.callback_query_handler(text="mega")
async def buy_xl(call):
    await call.message.answer(texts.XL_game, reply_markup=keyboards.buy_kb)
    await call.answer()


@dp.callback_query_handler(text="other")
async def buy_other(call):
    await call.message.answer(texts.other, reply_markup=keyboards.buy_kb)
    await call.answer()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
