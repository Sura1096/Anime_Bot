from aiogram.types import Message


def my_filter(message: Message):
    if not message.photo:
        return True
    return False
