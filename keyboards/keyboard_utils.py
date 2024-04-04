from anime_genres.genres_list import genres
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def user_choice_buttons():
    keyboard_builder = InlineKeyboardBuilder()
    category_buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text='Genres 📁',
                             callback_data='genres'),
        InlineKeyboardButton(text='Random anime 🃏',
                             callback_data='random anime'),
        InlineKeyboardButton(text='Popular anime 🔥',
                             callback_data='popular anime'),
        InlineKeyboardButton(text='Search by name 🔎',
                             callback_data='search anime')
    ]

    keyboard_builder.row(*category_buttons, width=1)
    return keyboard_builder


def help_command_button():
    admin_link = InlineKeyboardButton(text='Contact admin',
                                      url='https://t.me/Sura_1096')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[admin_link]])
    return keyboard


def genres_buttons():
    keyboard_builder = InlineKeyboardBuilder()
    genre_buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text=f'{genre}', callback_data=genres[genre]) for genre in genres
    ]

    option_buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text='Apply filter 🟢', callback_data='apply filter'),
        InlineKeyboardButton(text='To home page ⛩', callback_data='home page')
    ]

    keyboard_builder.row(*genre_buttons, width=3)
    keyboard_builder.row(*option_buttons, width=1)
    return keyboard_builder
