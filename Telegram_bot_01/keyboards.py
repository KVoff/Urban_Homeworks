from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # type: ignore
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [

            KeyboardButton(text='Стоимость'),
            KeyboardButton(text='О нас')
        ]
    ], resize_keyboard=True
)


catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Среднее', callback_data='medium')],
        [InlineKeyboardButton(text='Большое', callback_data='big')],
        [InlineKeyboardButton(text='Очень Большое', callback_data='mega')],
        [InlineKeyboardButton(text='other', callback_data='other')]
    ]
)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='купить', url='google.com')],
        [InlineKeyboardButton(text='назад', callback_data='back_to_catalog')]
    ]
)

admin_panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Пользователи', callback_data='users')],
        [InlineKeyboardButton(texts='Статистика', callback_data='stat')],
        [
            InlineKeyboardButton(texts='Блокировка',
                                 callback_data='block'),
            InlineKeyboardButton(texts='Разблокировка',
                                 callback_data='unblock')
        ]
    ]
)
