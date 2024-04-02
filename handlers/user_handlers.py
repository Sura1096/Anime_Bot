from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON
from keyboards.keyboard_utils import user_choice_buttons, help_command_button, genres_buttons


router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'],
                         reply_markup=user_choice_buttons())


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON['/help'],
                         reply_markup=help_command_button())


@router.message(F.text == 'Genre 📁')
async def process_genres_button(message: Message):
    await message.answer(text='Here is all genres',
                         reply_markup=genres_button().as_markup(one_time_keyboard=True,
                                                                resize_keyboard=True))