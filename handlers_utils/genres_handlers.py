from typing import List

from aiogram import Router
from aiogram.types import Message

from aiogram_widgets.pagination import KeyboardPaginator

from keyboards.keyboard_utils import ButtonsForCommands, ButtonsForGenres
from utils.paginator import create_paginator


class GenresHandler:
    @staticmethod
    async def process_genres_button(router: Router) -> KeyboardPaginator:
        """
        This function creates keyboard paginator for genres.

        Args:
            router (Router): The router object from aiogram

        Returns:
            KeyboardPaginator: An KeyboardPaginator instance
            with the genres choice buttons.
        """
        genres = await ButtonsForGenres.genres_buttons()
        apply_filter_button = await ButtonsForGenres.apply_filter_for_genres_button()
        home_button = await ButtonsForCommands.end_home_button()
        paginator = await create_paginator(
            main_buttons=genres,
            bottom_buttons=[apply_filter_button, home_button],
            router=router,
            amount_per_page=10,
            amount_per_row=(3, 3),
        )

        return paginator

    @staticmethod
    async def update_genres_message(
            message: Message,
            router: Router,
            selected_genres: List[int]
    ) -> None:
        """
        This function updates genre buttons based
        on the user's selected genres and returns button
        to the home page, and updated list of buttons.

        Args:
            message (Message): The message object from
            aiogram representing the message to be edited.
            router (Router): The router object from aiogram
            selected_genres (list): A list of selected genre
            IDs to update the button states accordingly.
        """
        edit_buttons = await ButtonsForGenres.edit_genres_buttons(selected_genres)
        apply_filter_button = await ButtonsForGenres.apply_filter_for_genres_button()
        home_button = await ButtonsForCommands.end_home_button()
        paginator = await create_paginator(
            main_buttons=edit_buttons,
            bottom_buttons=[apply_filter_button, home_button],
            router=router,
            amount_per_page=10,
            amount_per_row=(3, 3),
        )

        await message.edit_reply_markup(reply_markup=paginator.as_markup())
