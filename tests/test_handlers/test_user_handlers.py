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

        mock_answer.assert_awaited_once_with(
            text=LEXICON['/start'],
            reply_markup=user_choice_buttons().as_markup()
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

        mock_answer.assert_awaited_once_with(
            text=LEXICON['/help'],
            reply_markup=help_command_button()
        )