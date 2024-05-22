from aiogram.filters.state import State, StatesGroup


class SelectGenres(StatesGroup):
    selected_genres = State()