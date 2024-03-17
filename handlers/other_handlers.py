from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import (LEXICON)


router = Router()


@router.message()
async def rest_message_handler(message: Message):
    await message.answer(text=LEXICON['unknown'])
