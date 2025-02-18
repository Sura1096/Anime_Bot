from aiogram import F, Router
from aiogram.types import CallbackQuery

from handlers_utils.random_anime_handlers import RandomAnimeHandlers


router = Router()


@router.callback_query(F.data == 'random anime')
async def process_random_button(callback: CallbackQuery) -> None:
    """
    Handles the 'random anime' inline button click
    and sends information about a random anime.

    The additional buttons include:
    - Next: Repeats the process of selecting and displaying a random anime.
    - To home page: Returns the user to the initial menu.

    Args:
        callback (CallbackQuery): The callback query
        object from aiogram representing the incoming
        callback query when the 'random anime' button is clicked.

    """
    random_home_but, full_anime_info = await RandomAnimeHandlers.process_random_button()
    try:
        await callback.message.answer_photo(photo=full_anime_info["image"])
        await callback.message.answer(
            text=f'🎲 {full_anime_info["title"]}\n'
            f'🌸 {full_anime_info["type_anime"]}\n'
            f'🎬 {full_anime_info["eps"]}\n'
            f'🔥 {full_anime_info["status"]}\n'
            f'🌟 {full_anime_info["score"]}\n'
            f'📆 {full_anime_info["year"]}\n'
            f'🗂 {full_anime_info["genres"]}\n'
            f'📜 {full_anime_info["desc"]}\n'
            f'\n☆*:.｡.o(≧▽≦)o.｡.:*☆',
            parse_mode='html',
            reply_markup=random_home_but.as_markup(),
        )
    except Exception as e:
        await callback.message.answer(
            text='Oooops 👀\n'
            'Something went wrong ☠️.\n'
            'Please press the button "Next 🟢" one more time ⬆️.',
            reply_markup=random_home_but.as_markup(),
        )
    finally:
        await callback.answer()
