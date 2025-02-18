from aiogram import Router
from aiogram.types import Message

from filters.is_admin import my_filter


router = Router()


@router.message(my_filter)
async def rest_message_handler(message: Message) -> None:
    """
    Handles messages that do not match other
    specified handlers and deletes them.

    Args:
        message (Message): The message object from aiogram
        representing the incoming message.
    """
    await message.delete()
