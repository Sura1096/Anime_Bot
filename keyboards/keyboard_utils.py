from anime_genres.genres_list import genres
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def genres_button():
    kb_builder = ReplyKeyboardBuilder()

    buttons: list[KeyboardButton] = [
        KeyboardButton(text=f'{genre}') for genre in genres
    ]

    kb_builder.row(*buttons, width=4)
    return kb_builder