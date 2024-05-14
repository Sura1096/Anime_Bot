from aiogram import Router, F
from aiogram.types import Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent
import hashlib
from lexicon.lexicon import (LEXICON)
from Jikan_API.parse_data_from_api import ParseAnimeDataFromSearch
from Jikan_API.API import JikanAPI
from filters.is_admin import my_filter


router = Router()


@router.message(my_filter)
async def rest_message_handler(message: Message):
    await message.answer(text=LEXICON['unknown'])
