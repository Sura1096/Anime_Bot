from anime_genres.genres_list import genres
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def user_choice_buttons():
    genre_but = InlineKeyboardButton(text='Genre 📁',
                                     callback_data='genre')
    random_but = InlineKeyboardButton(text='Random anime 🃏',
                                      callback_data='random anime')
    popular_but = InlineKeyboardButton(text='Popular anime 🔥',
                                       callback_data='popular anime')
    search_but = InlineKeyboardButton(text='Search by name 🔎',
                                      callback_data='search anime')

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[genre_but],
                                                     [random_but],
                                                     [popular_but],
                                                     [search_but]])
    return keyboard


def help_command_button():
    admin_link = InlineKeyboardButton(text='Contact admin',
                                      url='https://t.me/Sura_1096')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[admin_link]])
    return keyboard


def genres_buttons():
    genre_buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text=f'{genre}', callback_data=genres[genre]) for genre in genres
    ]

    option_buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text='Apply filter 🟢', callback_data='apply filter'),
        InlineKeyboardButton(text='To home page ⛩', callback_data='home page')
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=[genre_buttons, option_buttons])
    return keyboard
