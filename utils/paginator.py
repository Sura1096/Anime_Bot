from typing import List, Optional

from aiogram.types import InlineKeyboardButton
from aiogram import Router

from aiogram_widgets.pagination import KeyboardPaginator


async def create_paginator(
        main_buttons: Optional[List[InlineKeyboardButton]],
        bottom_buttons: List[List[InlineKeyboardButton]],
        router: Router,
        amount_per_page: int,
        amount_per_row: tuple[int, int]
) -> KeyboardPaginator:
    """
    This function creates keyboard paginator for genres.

    Args:
        main_buttons (Optional[List[InlineKeyboardButton]]): Buttons data.
        bottom_buttons (List[List[InlineKeyboardButton]]): Provide additional
        buttons, that will be inserted after pagination panel.
        router (Router): The router object from aiogram.
        amount_per_page (int): Amount of items per page.
        amount_per_row (tuple[int, int]): Amount of items per row.

    Returns:
        KeyboardPaginator: An KeyboardPaginator instance
        with the genres choice buttons.
    """
    paginator = KeyboardPaginator(
        data=main_buttons,
        additional_buttons=bottom_buttons,
        router=router,
        per_page=amount_per_page,
        per_row=amount_per_row,
    )

    return paginator
