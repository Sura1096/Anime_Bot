from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON
from keyboards.keyboard_utils import (user_choice_buttons, help_command_button,
                                      genres_buttons, apply_filter_button, end_home_button)
from aiogram_widgets.pagination import KeyboardPaginator
from anime_genres.genres_list import genres


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
    buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text=f'{genres[genre_id]}', callback_data=str(genre_id)) for genre_id in genres
    ]

    home_buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text='Apply filter 🟢', callback_data='apply filter'),
        InlineKeyboardButton(text='To home page ⛩', callback_data='home page')
    ]

    paginator = KeyboardPaginator(
        data=buttons,
        additional_buttons=[home_buttons],
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