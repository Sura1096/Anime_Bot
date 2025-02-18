from aiogram import F, Router
from aiogram.types import CallbackQuery

from handlers_utils.popular_anime_handlers import PopularAnimeHandlers


router = Router()


@router.callback_query(F.data == 'popular anime')
async def process_popular_buttons(callback: CallbackQuery) -> None:
    """
    Handles the 'popular anime' inline button click
    and sends a list of popular anime buttons.

    Args:
        callback (CallbackQuery): The callback query
        object from aiogram representing the incoming
        callback query when the 'popular anime' button is clicked.
    """
    paginator = await PopularAnimeHandlers.process_popular_buttons(router)
    await callback.message.answer(
        text='Here is all popular anime 🔥', reply_markup=paginator.as_markup()
    )
    await callback.answer()
