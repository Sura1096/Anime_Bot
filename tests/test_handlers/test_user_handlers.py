import pytest
from unittest.mock import AsyncMock, patch
from aiogram.types import Chat
from types import SimpleNamespace

from Git.Anime_Bot.handlers.user_handlers import (process_start_command,
                                                  process_help_command,
                                                  process_home_page_button)
from Git.Anime_Bot.lexicon.lexicon import LEXICON
from Git.Anime_Bot.keyboards.keyboard_utils import (user_choice_buttons,
                                                    help_command_button)


@pytest.mark.asyncio
async def test_process_start_command():
    message = SimpleNamespace(
        message_id=1,
        date=0,
        chat=Chat(id=1, type='private'),
        text='/start',
        answer=AsyncMock()
    )

    with patch.object(message, 'answer', new=AsyncMock()) as mock_answer:
        await process_start_command(message)

        keyboard = await user_choice_buttons()
        mock_answer.assert_awaited_once_with(
            text=LEXICON['/start'],
            reply_markup=keyboard.as_markup()
        )


@pytest.mark.asyncio
async def test_process_help_command():
    message = SimpleNamespace(
        message_id=1,
        date=0,
        chat=Chat(id=1, type='private'),
        text='/help',
        answer=AsyncMock()
    )

    with patch.object(message, 'answer', new=AsyncMock()) as mock_answer:
        await process_help_command(message)

        keyboard = await help_command_button()
        mock_answer.assert_awaited_once_with(
            text=LEXICON['/help'],
            reply_markup=keyboard
        )


@pytest.mark.asyncio
async def test_process_home_page_button():
    message = SimpleNamespace(
        message_id=1,
        date=0,
        chat=Chat(id=1, type='private'),
        text='/start',
        answer=AsyncMock()
    )

    callback = SimpleNamespace(
        id='123',
        from_user=None,
        message=message,
        data='home page',
        chat_instance='123',
        answer=AsyncMock()
    )

    with (patch.object(message, 'answer', new=AsyncMock()) as mock_message_answer,
          patch.object(callback, 'answer', new=AsyncMock()) as mock_callback_answer):
        await process_home_page_button(callback)

        keyboard = await user_choice_buttons()
        mock_message_answer.assert_awaited_once_with(
            text=LEXICON['/start'],
            reply_markup=keyboard.as_markup()
        )

        mock_callback_answer.assert_awaited_once_with()
