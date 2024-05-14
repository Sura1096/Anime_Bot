from aiogram import Router, F
from aiogram.types import Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent
import hashlib
from lexicon.lexicon import (LEXICON)
from Jikan_API.parse_data_from_api import ParseAnimeDataFromSearch
from Jikan_API.API import JikanAPI


router = Router()


def my_filter(message: Message):
    if not message.text.startswith(':'):
        return True
    return False


@router.message(my_filter)
async def rest_message_handler(message: Message):
    await message.answer(text=LEXICON['unknown'])
