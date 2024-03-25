from anime_genres.genres_list import genres
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def genres_button():
    kb_builder = ReplyKeyboardBuilder()

    genre_buttons: list[KeyboardButton] = [
        KeyboardButton(text=f'{genre}') for genre in genres
    ]

    option_buttons: list[KeyboardButton] = [
        KeyboardButton(text='Apply filter 🟢'),
        KeyboardButton(text='To home page ⛩')
    ]

    kb_builder.row(*genre_buttons, width=4)
    kb_builder.row(*option_buttons, width=2)
    return kb_builder