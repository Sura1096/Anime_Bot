from jikanpy import Jikan
from typing import Dict


async def genres() -> Dict[int, str]:
    """
    Fetches and returns a dictionary of anime genres using the Jikan API.

    Returns: dict[int, str]: A dictionary mapping genre IDs to genre names.
    """
    anime = Jikan()
    data = anime.genres('anime')['data']
    genres_dict: dict[int, str] = {}

    for item in data:
        genres_dict[item['mal_id']] = item['name']

    return genres_dict
