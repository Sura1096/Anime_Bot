from typing import List, Optional

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from jikanpy import Jikan

from external_services.API import JikanAPI
from external_services.genres_list import genres


class ButtonsForCommands:
    @staticmethod
    async def user_choice_buttons() -> InlineKeyboardBuilder:
        """
        Create an inline keyboard with user choice buttons
        for various categories.

        Returns:
            InlineKeyboardBuilder: An InlineKeyboardBuilder
            instance with the user choice buttons.
        """
        keyboard_builder = InlineKeyboardBuilder()
        category_buttons: list[InlineKeyboardButton] = [
            InlineKeyboardButton(
                text='Genres 📁',
                callback_data='genres'
            ),
            InlineKeyboardButton(
                text='Random anime 🃏',
                callback_data='random anime'
            ),
            InlineKeyboardButton(
                text='Popular anime 🔥',
                callback_data='popular anime'
            ),
            InlineKeyboardButton(
                text='Search by name 🔎',
                switch_inline_query_current_chat=''
            ),
        ]

        keyboard_builder.row(*category_buttons, width=1)
        return keyboard_builder

    @staticmethod
    async def help_command_button() -> InlineKeyboardMarkup:
        """
        Create an inline keyboard button for contacting the admin.

        Returns:
            InlineKeyboardMarkup: An InlineKeyboardMarkup instance
            with the admin contact button.
        """
        admin_link = InlineKeyboardButton(
            text='Contact admin', url='https://t.me/S_1096'
        )
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[admin_link]])
        return keyboard

    @staticmethod
    async def end_home_button() -> List[InlineKeyboardButton]:
        """
        Create an inline keyboard button for returning to the home page.

        Returns:
            List[InlineKeyboardButton]: A list with one InlineKeyboardButton
            instance for returning to the home page.
        """
        home_button: list[InlineKeyboardButton] = [
            InlineKeyboardButton(
                text='To home page ⛩',
                callback_data='home page'
            )
        ]
        return home_button

    @staticmethod
    async def home_button_markup() -> InlineKeyboardMarkup:
        home_button = InlineKeyboardButton(
            text='To home page ⛩', callback_data='home page'
        )
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[home_button]])

        return keyboard


class ButtonsForGenres:
    @staticmethod
    async def genres_buttons() -> List[InlineKeyboardButton]:
        """
        Create inline keyboard buttons for each genre.

        Returns:
            List[InlineKeyboardButton]: A list of InlineKeyboardButton
            instances for genres.
        """
        genres_dict = await genres()
        buttons: list[InlineKeyboardButton] = [
            InlineKeyboardButton(
                text=f'🔴 {genres_dict[genre_id]}',
                callback_data='🔴_' + str(genre_id)
            )
            for genre_id in genres_dict
        ]
        return buttons

    @staticmethod
    async def edit_genres_buttons(
        selected_genres: List[int],
    ) -> List[InlineKeyboardButton]:
        """
        Create inline keyboard buttons for each genre with
        selected genres marked.

        Args:
            selected_genres (List[int]): A list of selected genre IDs.

        Returns:
            List[InlineKeyboardButton]: A list of InlineKeyboardButton
            instances with selected genres marked.
        """
        genres_dict = await genres()
        buttons = []
        for genre_id, genre_name in genres_dict.items():
            if genre_id in selected_genres:
                buttons.append(
                    InlineKeyboardButton(
                        text=f'🟢 {genre_name}', callback_data=f'🟢_{genre_id}'
                    )
                )
            else:
                buttons.append(
                    InlineKeyboardButton(
                        text=f'🔴 {genre_name}', callback_data=f'🔴_{genre_id}'
                    )
                )
        return buttons

    @staticmethod
    async def apply_filter_for_genres_button() -> List[InlineKeyboardButton]:
        """
        Create an inline keyboard button for applying the genre filter.

        Returns:
            List[InlineKeyboardButton]: A list with one InlineKeyboardButton
            instance for applying the filter.
        """
        apply_filter: list[InlineKeyboardButton] = [
            InlineKeyboardButton(
                text='Apply filter 🟢', callback_data='apply filter for genres'
            )
        ]
        return apply_filter

    @staticmethod
    async def genre_category_button() -> InlineKeyboardBuilder:
        keyboard_builder = InlineKeyboardBuilder()
        genre_category: list[InlineKeyboardButton] = [
            InlineKeyboardButton(
                text='Genres 📁',
                callback_data='genres'
            ),
            InlineKeyboardButton(
                text='To home page ⛩',
                callback_data='home page'
            ),
        ]
        keyboard_builder.row(*genre_category, width=1)
        return keyboard_builder

    @staticmethod
    async def genres_anime_buttons(
            params: str
    ) -> Optional[List[InlineKeyboardButton]]:
        """
         Create inline keyboard buttons for anime filtered by genres.

        Args:
            params (str): A comma-separated string of genre IDs to filter by.

        Returns:
            Optional[List[InlineKeyboardButton]]: A list of
            InlineKeyboardButton instances for the filtered anime,
            or None if no data is found.
        """
        anime = JikanAPI()
        data = await anime.search_by_genres_id({'genres': params})
        if data['data']:
            buttons: list[InlineKeyboardButton] = [
                InlineKeyboardButton(
                    text=f'⛩ {item["title"]}',
                    switch_inline_query_current_chat=f'{item["title"]}',
                )
                for item in data['data']
            ]
            return buttons
        return None


class ButtonsForRandom:
    @staticmethod
    async def random_home_buttons() -> InlineKeyboardBuilder:
        """
        Create inline keyboard buttons for getting another
        random anime or returning to the home page.

        Returns:
            InlineKeyboardBuilder: An InlineKeyboardBuilder
            instance with the random/home buttons.
        """
        keyboard_builder = InlineKeyboardBuilder()
        home_random_buttons: list[InlineKeyboardButton] = [
            InlineKeyboardButton(
                text='Next 🟢',
                callback_data='random anime'
            ),
            InlineKeyboardButton(
                text='To home page ⛩',
                callback_data='home page'
            ),
        ]
        keyboard_builder.row(*home_random_buttons, width=1)
        return keyboard_builder


class ButtonsForPopularAnime:
    @staticmethod
    async def popular_anime_buttons() -> List[InlineKeyboardButton]:
        """
        Create inline keyboard buttons for the top popular anime.

        Returns:
            List[InlineKeyboardButton]: A list of InlineKeyboardButton
            instances for the top popular anime.
        """
        anime = Jikan()
        data = anime.top('anime')
        buttons: list[InlineKeyboardButton] = [
            InlineKeyboardButton(
                text=f'⛩ {item["title"]}',
                switch_inline_query_current_chat=f'{item["title"]}',
            )
            for item in data['data']
        ]
        return buttons
