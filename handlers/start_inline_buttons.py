from aiogram import F, Router
from aiogram.types import CallbackQuery
from keyboards.keyboard_utils import (genres_buttons, apply_filter_for_genres_button, end_home_button,
                                      random_home_buttons, popular_anime_buttons, edit_genres_buttons,
                                      genres_anime_buttons, genre_category_button)
from aiogram_widgets.pagination import KeyboardPaginator
from external_services.random_anime import get_random_anime, random_anime
from aiogram.fsm.context import FSMContext
from states.states import SelectGenres


router = Router()


async def create_paginator(main_buttons, bottom_buttons, amount_per_page, amount_per_row):
    paginator = KeyboardPaginator(
        data=main_buttons,
        additional_buttons=bottom_buttons,
        router=router,
        per_page=amount_per_page,
        per_row=amount_per_row
    )

    return paginator


@router.callback_query(F.data == 'genres')
async def process_genres_button(callback: CallbackQuery, state: FSMContext):
    """
    Handles the 'Genres' inline button click and sends a paginated list of genre buttons.

    This handler is triggered when a user clicks the inline button labeled 'Genres'. It responds by
    creating a paginated list of genre buttons, along with additional buttons for applying filters
    and returning to the home page. The user can select genres from the paginated list.

    Args:
        - callback (CallbackQuery): The callback query object from aiogram representing the incoming
        callback query when the 'Genres' button is clicked.
        - state (FSMContext): The current state of the finite state machine for handling user interactions.
    """
    genres = await genres_buttons()
    apply_filter_button = await apply_filter_for_genres_button()
    home_button = await end_home_button()
    paginator = await create_paginator(
        genres,
        [apply_filter_button, home_button],
        10,
        (3, 3)
    )

    await state.set_state(SelectGenres.selected_genres)
    await callback.message.answer(text='Select genres ❤️‍🔥', reply_markup=paginator.as_markup())
    await callback.answer()


async def update_genres_message(message, selected_genres):
    """
    This function updates genre buttons based on the user's selected genres
    and returns button to the home page, and updated list of buttons.

    Args:
        message (Message): The message object from aiogram representing the message to be edited.
        selected_genres (list): A list of selected genre IDs to update the button states accordingly.
    """
    edit_buttons = await edit_genres_buttons(selected_genres)
    apply_filter_button = await apply_filter_for_genres_button()
    home_button = await end_home_button()
    paginator = await create_paginator(
        edit_buttons,
        [apply_filter_button, home_button],
        10,
        (3, 3)
    )
    await message.edit_reply_markup(reply_markup=paginator.as_markup())


@router.callback_query(SelectGenres.selected_genres, lambda c: c.data.startswith('🔴_'))
async def genre_select_handler(callback_query: CallbackQuery, state: FSMContext):
    """
    Handles the selection of a genre button, updates the selected genres, and modifies the genre button list.

    This handler is triggered when a user clicks an inline button representing a genre, identified by
    a data prefix '🔴_' (indicating the genre is not selected).
    It updates the state to reflect the user's selected genres, changing the button from '🔴' to '🟢' when
    a genre is selected. The updated list of genre buttons is then displayed.

    Args:
        callback_query (CallbackQuery): The callback query object from aiogram representing the
        incoming callback query when a genre button is clicked.
        state (FSMContext): The current state of the finite state machine for handling user interactions.
        """
    genre_id = int(callback_query.data.split('_')[1])

    data = await state.get_data()
    selected_genres = data.get('selected_genres', [])

    if genre_id not in selected_genres:
        selected_genres.append(genre_id)
        await state.update_data(selected_genres=selected_genres)

    await update_genres_message(callback_query.message, selected_genres)


@router.callback_query(SelectGenres.selected_genres, lambda c: c.data.startswith('🟢_'))
async def genre_unselect_handler(callback_query: CallbackQuery, state: FSMContext):
    """
    Handles the selection of a genre button, updates the selected genres, and modifies the genre button list.

    This handler is triggered when a user clicks an inline button representing a genre, identified by
    a data prefix '🟢_' (indicating the genre is selected).
    It updates the state to reflect the user's selected genres, changing the button from '🟢' to '🔴' when
    a genre is selected. The updated list of genre buttons is then displayed.

    Args:
        callback_query (CallbackQuery): The callback query object from aiogram representing the
        incoming callback query when a genre button is clicked.
        state (FSMContext): The current state of the finite state machine for handling user interactions.
    """
    genre_id = int(callback_query.data.split('_')[1])

    data = await state.get_data()
    selected_genres = data.get('selected_genres', [])

    if genre_id in selected_genres:
        selected_genres.remove(genre_id)
        await state.update_data(selected_genres=selected_genres)

    await update_genres_message(callback_query.message, selected_genres)


@router.callback_query(F.data == 'apply filter for genres')
async def apply_filter_handler(callback_query: CallbackQuery, state: FSMContext):
    """
    Handles the 'apply filter' button click, filters anime by selected genres, and displays the results.

    This handler is triggered when a user clicks the inline button labeled 'apply filter'. It retrieves
    the list of selected genres from the state, generates buttons for anime that match the selected genres, and
    displays the results in a paginated format. If no anime match the selected genres, it sends a message indicating
    that no matching anime were found.

    Args:
        callback_query (CallbackQuery): The callback query object from aiogram representing the incoming
        callback query when the 'apply filter for genres' button is clicked.
        state (FSMContext): The current state of the finite state machine for handling user interactions.
    """
    data = await state.get_data()
    selected_genres = data.get('selected_genres', [])
    ids = ', '.join(str(genre) for genre in selected_genres)
    generate_buttons = await genres_anime_buttons(ids)

    if generate_buttons:
        home_button = await end_home_button()
        paginator = await create_paginator(
            generate_buttons,
            [home_button],
            5,
            (1, 1)
        )
        await callback_query.message.answer(text='Here are all the anime of your chosen genres 🪭',
                                            reply_markup=paginator.as_markup())
    else:
        genre_category = await genre_category_button()
        await callback_query.message.answer(text='There is no anime with your selected genres 💔\n'
                                                 'Try choosing a different genre combination:з',
                                            reply_markup=genre_category.as_markup())
    await state.clear()
    await callback_query.answer()


@router.callback_query(F.data == 'random anime')
async def process_random_button(callback: CallbackQuery):
    """
    Handles the 'random anime' inline button click and sends information about a random anime.

    The additional buttons include:
    - Next: Repeats the process of selecting and displaying a random anime.
    - To home page: Returns the user to the initial menu.

    Args:
        callback (CallbackQuery): The callback query object from aiogram representing the incoming
        callback query when the 'random anime' button is clicked.

    """
    random_home_but = await random_home_buttons()
    try:
        anime_items = await get_random_anime()
        full_anime_info = await random_anime(anime_items)

        await callback.message.answer_photo(photo=full_anime_info["image"])
        await callback.message.answer(text=f'🎲 {full_anime_info["title"]}\n'
                                           f'🌸 {full_anime_info["type_anime"]}\n'
                                           f'🎬 {full_anime_info["eps"]}\n'
                                           f'🔥 {full_anime_info["status"]}\n'
                                           f'🌟 {full_anime_info["score"]}\n'
                                           f'📆 {full_anime_info["year"]}\n'
                                           f'🗂 {full_anime_info["genres"]}\n'
                                           f'📜 {full_anime_info["desc"]}\n'
                                           f'\n☆*:.｡.o(≧▽≦)o.｡.:*☆',
                                      parse_mode='html',
                                      reply_markup=random_home_but.as_markup())
    except Exception as e:
        await callback.message.answer(text='Oooops 👀\n'
                                           'Something went wrong ☠️.\n'
                                           'Please press the button "Next 🟢" one more time ⬆️.')
    finally:
        await callback.answer()


@router.callback_query(F.data == 'popular anime')
async def process_popular_buttons(callback: CallbackQuery):
    """
    Handles the 'popular anime' inline button click and sends a list of popular anime buttons.

    Args:
        callback (CallbackQuery): The callback query object from aiogram representing the incoming
        callback query when the 'popular anime' button is clicked.
    """
    paginator = KeyboardPaginator(
        data=popular_anime_buttons(),
        additional_buttons=[end_home_button()],
        router=router,
        per_page=5,
        per_row=(1, 1)
    )
    await callback.message.answer(text='Here is all popular anime 🔥',
                                  reply_markup=paginator.as_markup())
    await callback.answer()
