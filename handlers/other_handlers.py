from aiogram import Router
from aiogram.types import Message
from filters.is_admin import my_filter


router = Router()


@router.message(my_filter)
async def rest_message_handler(message: Message):
    await message.delete()
