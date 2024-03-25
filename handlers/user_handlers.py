from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON
from keyboards.set_menu import start_menu
from keyboards.keyboard_utils import genres_button


router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'],
                         reply_markup=start_menu().as_markup(one_time_keyboard=True,
                                                             resize_keyboard=True))


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON['/help'])


@router.message(F.text == 'Genre 📁')
async def process_genres_button(message: Message):
    await message.answer(text='Here is all genres',
                         reply_markup=genres_button().as_markup(one_time_keyboard=True,
                                                                resize_keyboard=True))