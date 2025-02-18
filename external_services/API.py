from typing import Any, Dict

import aiohttp
from aiohttp import ClientTimeout


class JikanAPI:
    """
    A Python interface for interacting with the Jikan API,
    which provides data about anime.

    Attributes:
        base_url (str): The base URL for the Jikan API.

    Methods:
        get_anime_by_id(anime_id: int):
            Retrieve details of an anime by its ID.

        genres():
            Retrieve a list of all anime genres.

        search_by_genres_id(params: dict):
            Search for anime by genre IDs.

        get_random_anime():
            Retrieve details of a random anime.

        get_searched_anime(anime_name_parameter: dict):
            Search for anime by name.
    """

    def __init__(self, base_url: str ="https://api.jikan.moe/v4") -> None:
        """
        Initialize the JikanAPI with a base URL.

        Args:
            base_url (str): The base URL for the Jikan API.
            Defaults to 'https://api.jikan.moe/v4'.

        Returns:
            JikanAPI: Instance of JikanAPI

        Examples:
            anime = JikanAPI()
        """
        self.base_url = base_url

    async def get_anime_by_id(self, anime_id: int) -> Dict[str, Any] | str:
        """
        Retrieve details of an anime by its ID.

        Args:
            anime_id (int): The ID of the anime to retrieve.

        Returns:
            dict: A dictionary containing the anime details if found.
            str: 'Not found' if the anime is not found or the request fails.

        Examples:
            anime.get_anime_by_id(5)
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f"{self.base_url}/anime/{anime_id}",
                    timeout=ClientTimeout(total=5)
            ) as res:
                if res.status != 200:
                    return "Not found"
                return await res.json()

    async def genres(self) -> Dict[str, Any] | str:
        """
        Retrieve a list of all anime genres.

        Returns:
            dict: A dictionary containing a list of all anime genres.
            str: 'Not found' if the request fails.

        Examples:
            anime.genres()
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f"{self.base_url}/genres/anime",
                    timeout=ClientTimeout(total=5)
            ) as res:
                if res.status != 200:
                    return "Not found"
                return await res.json()

    async def search_by_genres_id(
            self,
            params: Dict[str, str]
    ) -> Dict[str, Any] | str:
        """
        Search for anime by genre IDs.

        Args:
            params (dict): A dictionary containing query parameters,
            with 'genres' key holding a comma-separated string of genre IDs.

        Returns:
            dict: A dictionary containing the search results.
            str: 'Not found' if the search fails or no results are found.

        Example:
            anime.search_by_genres_id({'genres': '1, 2, 3'})
        """
        full_url = f"{self.base_url}/anime"
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    full_url,
                    params=params,
                    timeout=ClientTimeout(total=5)
            ) as res:
                if res.status != 200:
                    return "Not found"
                return await res.json()

    async def get_random_anime(self) -> Dict[str, Any] | str:
        """
        Retrieve details of a random anime.

        Returns:
            dict: A dictionary containing the random anime details if found.
            str: 'Not found' if the request fails.

        Example:
            anime.get_random_anime()
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f"{self.base_url}/random/anime",
                    timeout=ClientTimeout(total=5)
            ) as res:
                if res.status != 200:
                    return "Not found"
                return await res.json()

    async def get_searched_anime(
            self,
            anime_name_parameter: Dict[str, str]
    ) -> Dict[str, Any] | str:
        """
        Search for anime by name.

        Args:
            anime_name_parameter (dict): A dictionary containing
            query parameters, with 'q' key holding
            the anime name to search for.

        Returns:
            dict: A dictionary containing the search results.
            str: 'Not found' if the search fails or no results are found.

        Example:
            anime.get_searched_anime({'q': 'Oshi no ko'})
        """
        full_url = f"{self.base_url}/anime"
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    full_url,
                    params=anime_name_parameter,
                    timeout=ClientTimeout(total=5)
            ) as res:
                if res.status != 200:
                    return "Not found"
                return await res.json()
