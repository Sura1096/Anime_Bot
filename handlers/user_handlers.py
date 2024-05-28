from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON
from keyboards.keyboard_utils import (user_choice_buttons, help_command_button,
                                      genres_buttons, apply_filter_for_genres_button, end_home_button,
                                      random_home_buttons, popular_anime_buttons, edit_genres_buttons, genres_anime_buttons)


router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'],
                         reply_markup=user_choice_buttons().as_markup())


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON['/help'],
                         reply_markup=help_command_button())


@router.callback_query(F.data == 'home page')
async def process_home_page_button(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON['/start'],
                                  reply_markup=user_choice_buttons().as_markup())
    await callback.answer()
