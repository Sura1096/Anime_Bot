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
from Jikan_API.random_anime import get_random_anime, random_anime
from Jikan_API.parse_data_from_api import ParseAnimeDataFromSearch
from aiogram.fsm.context import FSMContext
from states.states import SelectGenres


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
    await state.set_state(SelectGenres.selected_genres)
    await callback.message.answer(text='Select genres ❤️‍🔥', reply_markup=paginator.as_markup())


async def update_genres_message(message, selected_genres):
    paginator = KeyboardPaginator(
        data=edit_genres_buttons(selected_genres),
        additional_buttons=[apply_filter_for_genres_button(), end_home_button()],
        router=router,
        per_page=10,
        per_row=(3, 3)
    )
    await message.edit_reply_markup(reply_markup=paginator.as_markup())


@router.callback_query(SelectGenres.selected_genres, lambda c: c.data.startswith('🔴_'))
async def genre_select_handler(callback_query: CallbackQuery, state: FSMContext):
    genre_id = int(callback_query.data.split('_')[1])

    data = await state.get_data()
    selected_genres = data.get('selected_genres', [])

    if genre_id not in selected_genres:
        selected_genres.append(genre_id)
        await state.update_data(selected_genres=selected_genres)

    await update_genres_message(callback_query.message, selected_genres)


@router.callback_query(SelectGenres.selected_genres, lambda c: c.data.startswith('🟢_'))
async def genre_unselect_handler(callback_query: CallbackQuery, state: FSMContext):
    genre_id = int(callback_query.data.split('_')[1])

    data = await state.get_data()
    selected_genres = data.get('selected_genres', [])

    if genre_id in selected_genres:
        selected_genres.remove(genre_id)
        await state.update_data(selected_genres=selected_genres)

    await update_genres_message(callback_query.message, selected_genres)


@router.callback_query(F.data == 'apply filter for genres')
async def apply_filter_handler(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    selected_genres = data.get('selected_genres', [])
    generate_buttons = genres_anime_buttons(', '.join(str(genre)) for genre in selected_genres)
    if generate_buttons:
        paginator = KeyboardPaginator(
            data=generate_buttons,
            additional_buttons=[end_home_button()],
            router=router,
            per_page=5,
            per_row=(1, 1)
        )
        await callback_query.message.answer(text='Here all anime with your selected genres 🪭',
                                            reply_markup=paginator.as_markup())
    else:
        await callback_query.message.answer(text='There is no anime with your selected genres 💔')
    await state.clear()
    await callback_query.answer()


@router.callback_query(F.data == 'home page')
async def process_home_page_button(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON['/start'],
                                  reply_markup=user_choice_buttons().as_markup())
    await callback.answer()


@router.callback_query(F.data == 'random anime')
async def process_random_button(callback: CallbackQuery):
    anime_items = get_random_anime()
    full_anime_info = random_anime(anime_items)

    await callback.message.answer_photo(photo=full_anime_info["image"])
    await callback.message.answer(text=f'🎲 {full_anime_info["title"]}\n'
                                       f'🌸 {full_anime_info["type_anime"]}\n'
                                       f'🎬 {full_anime_info["eps"]}\n'
                                       f'🔥 {full_anime_info["status"]}\n'
                                       f'🌟 {full_anime_info["score"]}\n'
                                       f'📆 {full_anime_info["year"]}\n'
                                       f'🗂 {full_anime_info["genres"]}\n'
                                       f'📜 {full_anime_info["desc"]}\n'
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
