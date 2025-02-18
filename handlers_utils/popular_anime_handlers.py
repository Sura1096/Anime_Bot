from aiogram import Router

from aiogram_widgets.pagination import KeyboardPaginator

from keyboards.keyboard_utils import ButtonsForCommands, ButtonsForPopularAnime
from utils.paginator import create_paginator


class PopularAnimeHandlers:
    @staticmethod
    async def process_popular_buttons(router: Router) -> KeyboardPaginator:
        """
        This function creates keyboard paginator for
        popular anime.

        Args:
            router (Router): The router object from aiogram
        """
        popular_anime = await ButtonsForPopularAnime.popular_anime_buttons()
        home_button = await ButtonsForCommands.end_home_button()
        paginator = await create_paginator(
            main_buttons=popular_anime,
            bottom_buttons=[home_button],
            router=router,
            amount_per_page=5,
            amount_per_row=(1, 1),
        )

        return paginator
