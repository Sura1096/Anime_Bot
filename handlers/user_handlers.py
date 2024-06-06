from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart

from lexicon.lexicon import LEXICON
from keyboards.keyboard_utils import ButtonsForCommands


router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    """
    Handles the /start command and sends a message with inline buttons for user options.

    Args:
        message (Message): The message object from aiogram representing the incoming /start command.
    """
    keyboard = await user_choice_buttons()
    await message.answer(text=LEXICON['/start'],
                         reply_markup=keyboard.as_markup())


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    """
    Handles the /help command and responds with a message informing the user to contact the
    admin for questions, complaints, or wishes, and includes an inline button that
    facilitates contacting the admin.

    Args:
        message (Message): The message object from aiogram representing the incoming /help command.
    """
    keyboard = await help_command_button()
    await message.answer(text=LEXICON['/help'],
                         reply_markup=keyboard)


@router.callback_query(F.data == 'home page')
async def process_home_page_button(callback: CallbackQuery):
    """
    Handles the 'To home page' inline button click and sends a message with user options.

    Args:
        callback (CallbackQuery): The callback query object from aiogram representing the
        incoming callback query when the 'To home page' button is clicked
    """
    keyboard = await user_choice_buttons()
    await callback.message.answer(text=LEXICON['/start'],
                                  reply_markup=keyboard.as_markup())
    await callback.answer()
