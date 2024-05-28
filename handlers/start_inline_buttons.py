from aiogram import F, Router
from aiogram.types import CallbackQuery
from keyboards.keyboard_utils import (user_choice_buttons, help_command_button,
                                      genres_buttons, apply_filter_for_genres_button, end_home_button,
                                      random_home_buttons, popular_anime_buttons, edit_genres_buttons, genres_anime_buttons)
from aiogram_widgets.pagination import KeyboardPaginator
from Jikan_API.random_anime import get_random_anime, random_anime
from aiogram.fsm.context import FSMContext
from states.states import SelectGenres


router = Router()


@router.callback_query(F.data == 'genres')
async def process_genres_button(callback: CallbackQuery, state: FSMContext):
    paginator = KeyboardPaginator(
        data=genres_buttons(),
        additional_buttons=[apply_filter_for_genres_button(), end_home_button()],
        router=router,
        per_page=10,
        per_row=(3, 3)
    )
    await state.set_state(SelectGenres.selected_genres)
    await callback.message.answer(text='Select genres ❤️‍🔥', reply_markup=paginator.as_markup())


async def update_genres_message(message, selected_genres):
    paginator = KeyboardPaginator(
        data=edit_genres_buttons(selected_genres),
        additional_buttons=[apply_filter_for_genres_button(), end_home_button()],
        router=router,
        per_page=10,
        per_row=(3, 3)
    )
    await message.edit_reply_markup(reply_markup=paginator.as_markup())


@router.callback_query(SelectGenres.selected_genres, lambda c: c.data.startswith('🔴_'))
async def genre_select_handler(callback_query: CallbackQuery, state: FSMContext):
    genre_id = int(callback_query.data.split('_')[1])

    data = await state.get_data()
    selected_genres = data.get('selected_genres', [])

    if genre_id not in selected_genres:
        selected_genres.append(genre_id)
        await state.update_data(selected_genres=selected_genres)

    await update_genres_message(callback_query.message, selected_genres)


@router.callback_query(SelectGenres.selected_genres, lambda c: c.data.startswith('🟢_'))
async def genre_unselect_handler(callback_query: CallbackQuery, state: FSMContext):
    genre_id = int(callback_query.data.split('_')[1])

    data = await state.get_data()
    selected_genres = data.get('selected_genres', [])

    if genre_id in selected_genres:
        selected_genres.remove(genre_id)
        await state.update_data(selected_genres=selected_genres)

    await update_genres_message(callback_query.message, selected_genres)


@router.callback_query(F.data == 'apply filter for genres')
async def apply_filter_handler(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    selected_genres = data.get('selected_genres', [])
    generate_buttons = genres_anime_buttons(', '.join(str(genre)) for genre in selected_genres)
    if generate_buttons:
        paginator = KeyboardPaginator(
            data=generate_buttons,
            additional_buttons=[end_home_button()],
            router=router,
            per_page=5,
            per_row=(1, 1)
        )
        await callback_query.message.answer(text='Here all anime with your selected genres 🪭',
                                            reply_markup=paginator.as_markup())
    else:
        await callback_query.message.answer(text='There is no anime with your selected genres 💔')
    await state.clear()
    await callback_query.answer()


@router.callback_query(F.data == 'random anime')
async def process_random_button(callback: CallbackQuery):
    anime_items = get_random_anime()
    full_anime_info = random_anime(anime_items)

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
                                  reply_markup=random_home_buttons().as_markup())
    await callback.answer()


@router.callback_query(F.data == 'popular anime')
async def process_popular_buttons(callback: CallbackQuery):
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
