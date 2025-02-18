from external_services.random_anime import RandomAnime
from keyboards.keyboard_utils import ButtonsForRandom


class RandomAnimeHandlers:
    @staticmethod
    async def process_random_button() -> tuple:
        """
        This function generates random anime info.

        Returns:
            tuple: Random home button and full anime information.
        """
        random_home_but = await ButtonsForRandom.random_home_buttons()
        anime_items = await RandomAnime.get_random_anime()
        full_anime_info = await RandomAnime.random_anime(anime_items)
        return random_home_but, full_anime_info
