from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from handlers_utils.genres_handlers import GenresHandler
from keyboards.keyboard_utils import ButtonsForCommands, ButtonsForGenres
from states.states import SelectGenres
from utils.paginator import create_paginator


router = Router()


@router.callback_query(F.data == "genres")
async def process_genres_button(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Handles the 'Genres' inline button click and sends
    a paginated list of genre buttons.

    This handler is triggered when a user clicks the inline
    button labeled 'Genres'. It responds by creating a
    paginated list of genre buttons, along with additional
    buttons for applying filters and returning
    to the home page. The user can select genres
    from the paginated list.

    Args:
        - callback (CallbackQuery): The callback query object
        from aiogram representing the incoming callback query
        when the 'Genres' button is clicked.
        - state (FSMContext): The current state of the finite
        state machine for handling user interactions.
    """
    await state.clear()
    paginator = await GenresHandler.process_genres_button(router)

    await state.set_state(SelectGenres.selected_genres)
    await callback.message.answer(
        text="Select genres ❤️‍🔥",
        reply_markup=paginator.as_markup()
    )
    await callback.answer()


@router.callback_query(
    SelectGenres.selected_genres,
    lambda c: c.data.startswith("🔴_")
)
async def genre_select_handler(
        callback_query: CallbackQuery,
        state: FSMContext
) -> None:
    """
    Handles the selection of a genre button, updates
    the selected genres, and modifies the genre button list.

    This handler is triggered when a user clicks an inline
    button representing a genre, identified by a data
    prefix '🔴_' (indicating the genre is not selected).
    It updates the state to reflect the user's selected
    genres, changing the button from '🔴' to '🟢' when
    a genre is selected. The updated list of genre buttons
    is then displayed.

    Args:
        callback_query (CallbackQuery): The callback query object
        from aiogram representing the incoming callback query
        when a genre button is clicked.
        state (FSMContext): The current state of the finite
        state machine for handling user interactions.
    """
    genre_id = int(callback_query.data.split("_")[1])

    data = await state.get_data()
    selected_genres = data.get("selected_genres", [])

    if genre_id not in selected_genres:
        selected_genres.append(genre_id)
        await state.update_data(selected_genres=selected_genres)

    await GenresHandler.update_genres_message(
        callback_query.message,
        router,
        selected_genres
    )


@router.callback_query(
    SelectGenres.selected_genres,
    lambda c: c.data.startswith("🟢_")
)
async def genre_unselect_handler(
        callback_query: CallbackQuery,
        state: FSMContext
) -> None:
    """
    Handles the selection of a genre button, updates
    the selected genres, and modifies the genre button list.

    This handler is triggered when a user clicks an inline button
    representing a genre, identified by a data prefix '🟢_'
    (indicating the genre is selected). It updates the state
    to reflect the user's selected genres, changing the button
    from '🟢' to '🔴' when a genre is selected.
    The updated list of genre buttons is then displayed.

    Args:
        callback_query (CallbackQuery): The callback query object
        from aiogram representing the incoming callback query
        when a genre button is clicked.
        state (FSMContext): The current state of the
        finite state machine for handling user interactions.
    """
    genre_id = int(callback_query.data.split("_")[1])

    data = await state.get_data()
    selected_genres = data.get("selected_genres", [])

    if genre_id in selected_genres:
        selected_genres.remove(genre_id)
        await state.update_data(selected_genres=selected_genres)

    await GenresHandler.update_genres_message(
        callback_query.message,
        router,
        selected_genres
    )


@router.callback_query(F.data == "apply filter for genres")
async def apply_filter_handler(
        callback_query: CallbackQuery,
        state: FSMContext
) -> None:
    """
    Handles the 'apply filter' button click, filters anime
    by selected genres, and displays the results.

    This handler is triggered when a user clicks the inline
    button labeled 'apply filter'. It retrieves the list of
    selected genres from the state, generates buttons for anime
    that match the selected genres, and displays the results
    in a paginated format. If no anime match the selected genres,
    it sends a message indicating that no matching anime were found.

    Args:
        callback_query (CallbackQuery): The callback query object
        from aiogram representing the incoming callback query
        when the 'apply filter for genres' button is clicked.
        state (FSMContext): The current state of the finite state
        machine for handling user interactions.
    """
    data = await state.get_data()
    selected_genres = data.get("selected_genres", [])
    ids = ", ".join(str(genre) for genre in selected_genres)
    generate_buttons = await ButtonsForGenres.genres_anime_buttons(ids)

    if generate_buttons:
        home_button = await ButtonsForCommands.end_home_button()
        paginator = await create_paginator(
            main_buttons=generate_buttons,
            bottom_buttons=[home_button],
            router=router,
            amount_per_page=5,
            amount_per_row=(1, 1),
        )
        await callback_query.message.answer(
            text="Here are all the anime of your chosen genres 🪭",
            reply_markup=paginator.as_markup(),
        )
    else:
        genre_category = await ButtonsForGenres.genre_category_button()
        await callback_query.message.answer(
            text="There is no anime with your selected genres 💔"
                 "\nTry choosing a different genre combination:з",
            reply_markup=genre_category.as_markup(),
        )
    await state.clear()
    await callback_query.answer()
