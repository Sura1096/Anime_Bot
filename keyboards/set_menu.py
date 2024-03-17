from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def start_menu():
    genre_type_year_button = KeyboardButton(text='Genre, type and year 📁')
    random_button = KeyboardButton(text='Random anime 🃏')
    popular_button = KeyboardButton(text='Popular anime 🔥')
    search_button = KeyboardButton(text='Search by name 🔎')
    keyboard = ReplyKeyboardMarkup(keyboard=[[genre_type_year_button, random_button, popular_button, search_button]],
                                   one_time_keyboard=True,
                                   resize_keyboard=True)
    return keyboard