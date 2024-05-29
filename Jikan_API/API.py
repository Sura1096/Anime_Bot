import requests


class JikanAPI:
    """
    A Python interface for interacting with the Jikan API, which provides data about anime.

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
    def __init__(self, base_url='https://api.jikan.moe/v4'):
        self.base_url = base_url

    def get_anime_by_id(self, anime_id: int):
        """
        Retrieve details of an anime by its ID.

        Args:
            anime_id (int): The ID of the anime to retrieve.

        Returns:
            dict: A dictionary containing the anime details if found.
            str: 'Not found' if the anime is not found or the request fails.
        """
        res = requests.get(f'{self.base_url}/anime/{anime_id}')
        if res.status_code != 200:
            return 'Not found'
        return res.json()

    def genres(self):
        """
        Retrieve a list of all anime genres.

        Returns:
            dict: A dictionary containing a list of all anime genres.
            str: 'Not found' if the request fails.
        """
        res = requests.get(f'{self.base_url}/genres/anime')
        if res.status_code != 200:
            return 'Not found'
        return res.json()

    def search_by_genres_id(self, params):
        """
        Search for anime by genre IDs.

        Args:
            params (dict): A dictionary containing query parameters,
            with 'genres' key holding a comma-separated string of genre IDs.

        Returns:
            dict: A dictionary containing the search results.
            str: 'Not found' if the search fails or no results are found.

        Example of an input params:
            params = {
                "genres": "1,2,3"
                }
        """
        full_url = f'{self.base_url}/anime'
        res = requests.get(full_url, params=params)
        if res.status_code != 200:
            return 'Not found'
        return res.json()

    def get_random_anime(self):
        """
        Retrieve details of a random anime.

        Returns:
            dict: A dictionary containing the random anime details if found.
            str: 'Not found' if the request fails.
        """
        res = requests.get(f'{self.base_url}/random/anime')
        if res.status_code != 200:
            return 'Not found'
        return res.json()

    def get_searched_anime(self, anime_name_parameter):
        """
        Search for anime by name.

        Args:
            anime_name_parameter (dict): A dictionary containing query parameters,
            with 'q' key holding the anime name to search for.

        Returns:
            dict: A dictionary containing the search results.
            str: 'Not found' if the search fails or no results are found.

        Example of an input params:
            params = {
                "genres": "1,2,3" Replace with users parameters
                }
        """
        full_url = f'{self.base_url}/anime'
        res = requests.get(full_url, params=anime_name_parameter)
        if res.status_code != 200:
            return 'Not found'
        return res.json()
