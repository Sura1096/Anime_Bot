from aiogram import Router
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent
import hashlib
from Jikan_API.API import JikanAPI
from Jikan_API.parse_data_from_api import ParseAnimeDataFromSearch


router = Router()


@router.inline_query()
async def inline_mode(inline_query: InlineQuery):
    text = inline_query.query or 'Echo'
    param = {'q': text.capitalize()}
    anime = JikanAPI()
    data = anime.get_searched_anime(param)
    parse = ParseAnimeDataFromSearch(data)
    image = parse.anime_image()
    title = parse.anime_title()
    score = parse.anime_score()
    year = parse.anime_year()
    genres = parse.anime_included_genres_or_themes()
    desc = parse.anime_description()
    type_anime = parse.anime_type()
    eps = parse.anime_episodes()
    status = parse.anime_status()

    input_content = InputTextMessageContent(message_text=f'⛩ <b>Titles:</b> {title}\n'
                                                         f'🌸 {type_anime}\n'
                                                         f'🎬 <b>Episodes amount:</b> {eps}\n'
                                                         f'🔥 <b>Status:</b> {status}\n'
                                                         f'🌟 <b>Score:</b> {score}\n'
                                                         f'📆 {year}\n'
                                                         f'🗂 {genres}\n'
                                                         f'📜 {desc}\n'
                                                         f'\n☆*:.｡.o(≧▽≦)o.｡.:*☆'
                                                         f'\n🌌 <a href="{image}">Image:</a>',
                                            parse_mode='html')
    result_id = hashlib.md5(text.encode()).hexdigest()

    articles = InlineQueryResultArticle(
        id=result_id,
        title=f'⛩ {title}',
        input_message_content=input_content,
        thumbnail_url=image,
        description=f'🌟 Score: {score}, 🔥 Status: {status}, 🎬 Episodes: {eps}'
    )

    await inline_query.answer(results=[articles], cache_time=1, is_personal=True)
