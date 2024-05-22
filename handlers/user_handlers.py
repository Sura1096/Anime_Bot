from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, InlineQuery, InlineQueryResultArticle, InputTextMessageContent
import hashlib
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON
from keyboards.keyboard_utils import (user_choice_buttons, help_command_button,
                                      genres_buttons, apply_filter_for_genres_button, end_home_button,
                                      random_home_buttons, popular_anime_buttons, edit_genres_buttons, genres_anime_buttons)
from aiogram_widgets.pagination import KeyboardPaginator
from Jikan_API.API import JikanAPI
from Jikan_API.parse_data_from_api import ParseAnimeData, ParseAnimeDataFromSearch
from aiogram.fsm.context import FSMContext


router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'],
                         reply_markup=user_choice_buttons().as_markup())


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON['/help'],
                         reply_markup=help_command_button())


@router.callback_query(F.data == 'genres')
async def process_genres_button(callback: CallbackQuery, state: FSMContext):
    paginator = KeyboardPaginator(
        data=genres_buttons(),
        additional_buttons=[apply_filter_for_genres_button(), end_home_button()],
        router=router,
        per_page=10,
        per_row=(3, 3)
    )
    await callback.message.answer(text='Here is all genres 🗂',
                                  reply_markup=paginator.as_markup())
    await callback.answer()


@router.callback_query(F.data == 'home page')
async def process_home_page_button(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON['/start'],
                                  reply_markup=user_choice_buttons().as_markup())
    await callback.answer()


@router.callback_query(F.data == 'random anime')
async def process_random_button(callback: CallbackQuery):
    anime = JikanAPI()
    data = anime.get_random_anime()
    while data == 'Not found':
        data = anime.get_random_anime()
    parse = ParseAnimeData(data)
    image = parse.anime_image()
    title = parse.anime_title()
    score = parse.anime_score()
    year = parse.anime_year()
    genres = parse.anime_included_genres_or_themes()
    desc = parse.anime_description()
    type_anime = parse.anime_type()
    eps = parse.anime_episodes()
    status = parse.anime_status()

    while (score is None) or (genres is None) or (desc is None):
        anime = JikanAPI()
        data = anime.get_random_anime()
        while data == 'Not found':
            data = anime.get_random_anime()
        parse = ParseAnimeData(data)
        image = parse.anime_image()
        title = parse.anime_title()
        score = parse.anime_score()
        year = parse.anime_year()
        genres = parse.anime_included_genres_or_themes()
        desc = parse.anime_description()
        type_anime = parse.anime_type()
        eps = parse.anime_episodes()
        status = parse.anime_status()

    await callback.message.answer_photo(photo=image)
    await callback.message.answer(text=f'🎲 {title}\n'
                                       f'🌸 {type_anime}\n'
                                       f'🎬 {eps}\n'
                                       f'🔥 {status}\n'
                                       f'🌟 {score}\n'
                                       f'📆 {year}\n'
                                       f'🗂 {genres}\n'
                                       f'📜 {desc}\n'
                                       f'\n☆*:.｡.o(≧▽≦)o.｡.:*☆',
                                  parse_mode='html',
                                  reply_markup=random_home_buttons().as_markup())
    await callback.answer()


@router.callback_query(F.data == 'popular anime')
async def process_popular_buttons(callback: CallbackQuery):
    paginator = KeyboardPaginator(
        data=popular_anime_buttons(),
        additional_buttons=[end_home_button()],
        router=router,
        per_page=5,
        per_row=(1, 1)
    )
    await callback.message.answer(text='Here is all popular anime 🔥',
                                  reply_markup=paginator.as_markup())
    await callback.answer()


@router.inline_query()
async def inline_mode(inline_query: InlineQuery):
    text = inline_query.query or 'Echo'
    param = {'q': text}
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
                                                         f'\n🌌 <b>Image URL:</b>'
                                                         f'\n{image}\n'
                                                         f'\n☆*:.｡.o(≧▽≦)o.｡.:*☆',
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
