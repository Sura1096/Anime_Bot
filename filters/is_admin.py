from aiogram.types import Message


def my_filter(message: Message):
    if not message.text.startswith(':'):
        return True
    return False
