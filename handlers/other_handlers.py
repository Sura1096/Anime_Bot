from aiogram import Router, F
from aiogram.types import Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent
import hashlib
from lexicon.lexicon import (LEXICON)
from Jikan_API.parse_data_from_api import ParseAnimeDataFromSearch
from Jikan_API.API import JikanAPI


router = Router()
anime = JikanAPI()


@router.inline_query(F.data)
async def inline_echo(inline_query: InlineQuery):
    text = inline_query.query or 'Echo'
    input_content = InputTextMessageContent(message_text=text)
    result_id = hashlib.md5(text.encode()).hexdigest()

    item = [InlineQueryResultArticle(
        id=result_id,
        title='Text',
        input_message_content=input_content
    )]
    await inline_query.answer(results=item, is_personal=True)


@router.message()
async def rest_message_handler(message: Message):
    await message.answer(text=LEXICON['unknown'])
