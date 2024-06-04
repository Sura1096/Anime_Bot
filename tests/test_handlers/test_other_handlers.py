import pytest
from unittest.mock import AsyncMock, patch
from types import SimpleNamespace
from aiogram.types import Chat

from Git.Anime_Bot.handlers.other_handlers import rest_message_handler
from Git.Anime_Bot.filters.is_admin import my_filter


@pytest.mark.asyncio
async def test_my_filter():
    message = SimpleNamespace(text='⛩ Titles: something')
    assert not my_filter(message)

    message.text = 'Some other text'
    assert my_filter(message)


@pytest.mark.asyncio
async def test_rest_message_handler():
    message = SimpleNamespace(
        message_id=1,
        date=0,
        chat=Chat(id=1, type='private'),
        text='Some other text',
        delete=AsyncMock()
    )

    with patch.object(message, 'delete', new=AsyncMock()) as mock_delete:
        await rest_message_handler(message)

        mock_delete.assert_awaited_once()


@pytest.mark.asyncio
async def test_rest_message_handler_filter():
    message = SimpleNamespace(
        message_id=1,
        date=0,
        chat=Chat(id=1, type='private'),
        text='⛩ Titles: something',
        delete=AsyncMock()
    )
    if not my_filter(message):
        with patch.object(message, 'delete', new=AsyncMock()) as mock_delete:
            await rest_message_handler(message)
            mock_delete.assert_awaited_once()
    else:
        with patch.object(message, 'delete', new=AsyncMock()) as mock_delete:
            await rest_message_handler(message)
            mock_delete.assert_not_awaited()
