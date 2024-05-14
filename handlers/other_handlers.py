from aiogram import Router, F
from aiogram.types import Message
from lexicon.lexicon import (LEXICON)
from filters.is_admin import my_filter


router = Router()


@router.message(my_filter)
async def rest_message_handler(message: Message):
    await message.answer(text=LEXICON['unknown'])
