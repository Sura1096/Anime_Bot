from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON
from keyboards.keyboard_utils import (user_choice_buttons, help_command_button,
                                      genres_buttons, apply_filter_for_genres_button, end_home_button,
                                      random_home_buttons)
from aiogram_widgets.pagination import KeyboardPaginator
from Jikan_API.API import JikanAPI
from Jikan_API.parse_data_from_api import ParseAnimeData


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
async def process_genres_buttons(callback: CallbackQuery):
    paginator = KeyboardPaginator(
        data=genres_buttons(),
        additional_buttons=[apply_filter_for_genres_button(), end_home_button()],
        router=router,
        per_page=10,
        per_row=(3, 3)
    )
    await callback.message.answer(text='Here is all genres 🗂',
                                  reply_markup=paginator.as_markup())


@router.callback_query(F.data == 'home page')
async def process_home_page_button(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON['/start'],
                                  reply_markup=user_choice_buttons().as_markup())


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
    await callback.message.answer(text=f'{title} 🎲\n'
                                       f'{type_anime} 🌸\n'
                                       f'{eps} 🎬\n'
                                       f'{status} 🔥\n'
                                       f'{score} 🌟\n'
                                       f'{year} 📆\n'
                                       f'{genres} 🗂\n'
                                       f'📜 {desc}\n'
                                       f'\n☆*:.｡.o(≧▽≦)o.｡.:*☆',
                                  parse_mode='html',
                                  reply_markup=random_home_buttons().as_markup())