from aiogram import Router
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent
import hashlib
from external_services.API import JikanAPI
from external_services.parse_data_from_api import ParseAnimeDataFromSearch


router = Router()


@router.inline_query()
async def inline_mode(inline_query: InlineQuery):
    """
    Handles inline queries and returns search results for anime based on the user's input.

    This handler is triggered when the bot receives an inline query from a user. It processes the
    query, searches for matching anime using the Jikan API, and formats the results into a structured
    response that includes the anime's title, type, number of episodes, status, score, release year,
    genres, description, and an image link.

    Args:
        inline_query (InlineQuery): The inline query object from aiogram representing the incoming
        inline query from the user.
    """
    text = inline_query.query or 'Echo'
    param = {'q': text.capitalize()}
    anime = JikanAPI()
    data = await anime.get_searched_anime(param)
    parse = ParseAnimeDataFromSearch(data)
    image = await parse.anime_image()
    title = await parse.anime_title()
    score = await parse.anime_score()
    year = await parse.anime_year()
    genres = await parse.anime_included_genres_or_themes()
    desc = await parse.anime_description()
    type_anime = await parse.anime_type()
    eps = await parse.anime_episodes()
    status = await parse.anime_status()

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
