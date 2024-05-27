from aiogram.types import Message


def my_filter(message: Message):
    """
    Filter function for rest_message_handler.

    Args:
        message (Message): The message object from aiogram representing the incoming message.

    Returns:
        bool: True if the message does not start with '⛩ Titles:', otherwise False.
    """
    if not message.text.startswith('⛩ Titles:'):
        return True
    return False
