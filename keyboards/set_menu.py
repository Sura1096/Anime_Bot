from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def start_menu():
    kb_builder = ReplyKeyboardBuilder()

    buttons: list[KeyboardButton] = [
        KeyboardButton(text='Genre 📁'),
        KeyboardButton(text='Random anime 🃏'),
        KeyboardButton(text='Popular anime 🔥'),
        KeyboardButton(text='Search by name 🔎')
    ]

    kb_builder.row(*buttons, width=1)
    return kb_builder