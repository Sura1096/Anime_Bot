from aiogram.types import Message


def my_filter(message: Message):
    if not message.text.startswith('Titles:'):
        return True
    return False
