import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


load_dotenv("/usr//local/.env")

bot = Bot(os.getenv("API_Ub"))
dp = Dispatcher(bot, storage=MemoryStorage())

product1 = 1
product2 = 2
product3 = 3
product4 = 4

kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Информация'),
            KeyboardButton(text='Рассчитать')
            ], 
        [
            KeyboardButton(text='Купить')
            ]
        ],
    resize_keyboard=True
)

kb_inline = InlineKeyboardMarkup(resize_keyboard=True)
button_inl_1 = InlineKeyboardButton(text='Рассчитать норму калорий',
                                    callback_data='calories')
button_inl_2 = InlineKeyboardButton(text='Формулы расчёта',
                                    callback_data='formulas')
kb_inline.add(button_inl_1)
kb_inline.add(button_inl_2)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text='Product1', callback_data='product_buying'),
            InlineKeyboardButton(text='Product2', callback_data='product_buying'),
            InlineKeyboardButton(text='Product3', callback_data='product_buying'),
            InlineKeyboardButton(text='Product4', callback_data='product_buying')
        ]
    ],
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет!!!', reply_markup=kb)


@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer('Bot version: 0.02')


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_inline)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    await message.answer(
        f'Название: Product{product1} | '
        f'Описание: описание {product1} | '
        f'Цена: {product1 * 100}'
)
    with open('module_14/foto/1.png', 'rb')as img:
        await message.answer_photo(img)
    
    await message.answer(
        f'Название: Product{product2} | '
        f'Описание: описание {product2} | '
        f'Цена: {product2 * 100}'
)
    with open('module_14/foto/2.png', 'rb')as img:
        await message.answer_photo(img)

    await message.answer(
        f'Название: Product{product3} | '
        f'Описание: описание {product3} | '
        f'Цена: {product3 * 100}'
)
    with open('module_14/foto/3.png', 'rb')as img:
        await message.answer_photo(img)

    await message.answer(
        f'Название: Product{product4} | '
        f'Описание: описание {product4} | '
        f'Цена: {product4 * 100}'
)
    with open('module_14/foto/4.png', 'rb')as img:
        await message.answer_photo(img)

    await message.answer('Выберите продукт для покупки:', reply_markup=catalog_kb)
 

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    



@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см)'
                              ' – 5 х возраст (г) + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    man_Calories = 10 * int(data['weight']) + 6.5 * int(data['growth'])
    - 5 * int(data['age']) - 161

    await message.answer(man_Calories)
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
