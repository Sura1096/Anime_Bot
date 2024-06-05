import pytest
from aiogram.types import InlineKeyboardMarkup
from aiogram.fsm.state import State
from aiogram import Router

from Git.Anime_Bot.handlers.start_inline_buttons import (process_genres_button,
                                                         genre_select_handler,
                                                         genre_unselect_handler,
                                                         apply_filter_handler)
from Git.Anime_Bot.states.states import SelectGenres


router = Router()


class MockMessage:
    def __init__(self):
        self.reply_markup = None
        self.text = None

    async def answer(self, text, reply_markup):
        self.text = text
        self.reply_markup = reply_markup

    async def edit_reply_markup(self, reply_markup):
        self.reply_markup = reply_markup


class MockFSMContext:
    def __init__(self):
        self.state = None
        self.data = {}

    async def set_state(self, state: State):
        self.state = state

    async def get_data(self):
        return self.data

    async def update_data(self, **kwargs):
        self.data.update(kwargs)

    async def clear(self):
        self.data.clear()


class MockCallbackQuery:
    def __init__(self, data, message):
        self.data = data
        self.message = message

    async def answer(self):
        pass


@pytest.mark.asyncio
async def test_process_genres_button():
    message = MockMessage()
    state = MockFSMContext()
    callback_query = MockCallbackQuery(data='genres', message=message)

    await process_genres_button(callback_query, state)

    assert state.state == SelectGenres.selected_genres
    assert message.text == 'Select genres ❤️‍🔥'
    assert isinstance(message.reply_markup, InlineKeyboardMarkup)
    assert len(message.reply_markup.inline_keyboard) > 0

    buttons = message.reply_markup.inline_keyboard
    all_buttons = [btn for row in buttons for btn in row]
    assert any(btn.callback_data.startswith('🔴_') for btn in all_buttons)
    assert any(btn.callback_data == 'apply filter for genres' for btn in all_buttons)
    assert any(btn.callback_data == 'home page' for btn in all_buttons)


@pytest.mark.asyncio
async def test_genre_select_handler():
    message = MockMessage()
    state = MockFSMContext()
    callback_query = MockCallbackQuery(data='🔴_1', message=message)
    state.data = {'selected_genres': []}

    await genre_select_handler(callback_query, state)

    assert state.data['selected_genres'] == [1]
    assert isinstance(message.reply_markup, InlineKeyboardMarkup)


@pytest.mark.asyncio
async def test_genre_unselect_handler():
    message = MockMessage()
    state = MockFSMContext()
    callback_query = MockCallbackQuery(data='🟢_1', message=message)
    state.data = {'selected_genres': [1]}

    await genre_unselect_handler(callback_query, state)

    assert state.data['selected_genres'] == []
    assert isinstance(message.reply_markup, InlineKeyboardMarkup)


@pytest.mark.asyncio
async def test_apply_filter_handler():
    pass
