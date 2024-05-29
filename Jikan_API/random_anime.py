from .API import JikanAPI
from .parse_data_from_api import ParseAnimeData
from typing import Dict


async def get_random_anime() -> tuple:
    """
    Retrieve and parse data of a random anime.

    This function uses the JikanAPI to fetch data of a random anime and then parses
    the data to extract specific information.

    Returns:
        tuple: A tuple containing the following elements in order:
            - image (str): The URL of the anime's image.
            - title (str): The title(s) of the anime.
            - score (str): The score of the anime.
            - year (str): The release year of the anime.
            - genres (str): The genres or themes of the anime.
            - desc (str): The description (synopsis) of the anime.
            - type_anime (str): The type of the anime (e.g., TV, Movie).
            - eps (str): The number of episodes of the anime.
            - status (str): The status of the anime (e.g., Airing, Finished).
    """
    anime = JikanAPI()
    data = await anime.get_random_anime()
    while data == 'Not found':
        data = anime.get_random_anime()
    parse = ParseAnimeData(data)
    image = parse.anime_image()
    title = parse.anime_title()
    score = parse.anime_score()
    year = parse.anime_year()
    genres = parse.anime_included_genres_or_themes()
    desc = parse.anime_description()
    type_anime = parse.anime_type()
    eps = parse.anime_episodes()
    status = parse.anime_status()

    return image, title, score, year, genres, desc, type_anime, eps, status


def random_anime(anime_info) -> Dict[str, str]:
    """
    Convert a tuple of anime information into a dictionary.

    Args:
        anime_info (tuple): A tuple containing the following elements in order:
            - image (str): The URL of the anime's image.
            - title (str): The title(s) of the anime.
            - score (str): The score of the anime.
            - year (str): The release year of the anime.
            - genres (str): The genres or themes of the anime.
            - desc (str): The description (synopsis) of the anime.
            - type_anime (str): The type of the anime (e.g., TV, Movie).
            - eps (str): The number of episodes of the anime.
            - status (str): The status of the anime (e.g., Airing, Finished).

    Returns:
        Dict[str, str]: A dictionary with the following keys and their corresponding values from the tuple:
            - 'image': The URL of the anime's image.
            - 'title': The title(s) of the anime.
            - 'score': The score of the anime.
            - 'year': The release year of the anime.
            - 'genres': The genres or themes of the anime.
            - 'desc': The description (synopsis) of the anime.
            - 'type_anime': The type of the anime (e.g., TV, Movie).
            - 'eps': The number of episodes of the anime.
            - 'status': The status of the anime (e.g., Airing, Finished).
    """
    random_anime_dict = {}
    info_items = ['image', 'title', 'score', 'year', 'genres', 'desc',
                  'type_anime', 'eps', 'status']
    for i in range(len(anime_info)):
        random_anime_dict[info_items[i]] = anime_info[i]

    return random_anime_dict
