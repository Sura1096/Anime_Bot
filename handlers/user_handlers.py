from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON
from keyboards.keyboard_utils import user_choice_buttons, help_command_button, genres_buttons
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

    paginator = KeyboardPaginator(
        data=buttons,
        router=router,
        per_page=10,
        per_row=(3, 3)
    )
    await callback.message.answer(text='Here is all genres 🗂',
                                  reply_markup=paginator.as_markup())