from aiogram.filters.state import State, StatesGroup


class SelectGenres(StatesGroup):
    """
    State management for selecting genres in a bot.

    Attributes:
        selected_genres (State): The state representing the selection of genres by the user.
    """
    selected_genres = State()
