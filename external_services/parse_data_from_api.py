class ParseAnimeData:
    """
    A class for parsing anime data retrieved from the Jikan API.

    Attributes:
        anime (dict): The anime data to parse, defaults to 'Not found'.
    """
    def __init__(
            self,
            anime_data='Not found'
    ) -> None:
        """
        Initialize the ParseAnimeData with anime data.

        Args:
            anime_data (dict): The anime data to parse. Defaults to 'Not found'.

        Examples:
            parse_data = ParseAnimeData(anime_data)
        """
        self.anime = anime_data

    async def anime_image(self) -> str:
        """
        Retrieve the image URL of the anime.

        Returns:
            str: The image URL if available, otherwise a message indicating no image is available.

        Example:
            parse_data.anime_image()
        """
        res = self.anime['data']
        if res['images']:
            if res['images']['jpg']['image_url']:
                return res['images']['jpg']['image_url']
        return '<i>Image has not been added to this title.</i>'

    async def anime_title(self) -> str:
        """
        Retrieve the titles of the anime.

        Returns:
            str: A formatted string of the anime's titles.

        Example:
            parse_data.anime_title()
        """
        res = self.anime['data']
        titles = []
        if res['title_english']:
            titles.append(res['title_english'])
        if res['title']:
            titles.append(res['title'])
        return f"<b>Titles:</b> {' / '.join(titles)}"

    async def anime_score(self) -> str:
        """
        Retrieve the score of the anime.

        Returns:
            str: The anime's score if available, otherwise a message indicating no score is available.

        Example:
            parse_data.anime_score()
        """
        res = self.anime['data']
        if res['score']:
            return f"<b>Score:</b> {res['score']}"
        else:
            return "<i>No score information has been added to this title.</i>"

    async def anime_year(self) -> str:
        """
        Retrieve the release year of the anime.

        Returns:
            str: The release year if available, otherwise a message indicating no year is available.

        Example:
            parse_data.anime_year()
        """
        res = self.anime['data']
        if res['year']:
            return f"<b>Year:</b> {res['year']}"
        else:
            return "<i>No year information has been added to this title.</i>"

    async def anime_included_genres_or_themes(self) -> str:
        """
        Retrieve the genres or themes of the anime.

        Returns:
            str: A formatted string of the anime's genres or themes if available,
            otherwise a message indicating no genres or themes are available.

        Example:
            parse_data.anime_included_genres_or_themes()
        """
        res = self.anime['data']
        genres = []
        themes = []
        if res['genres']:
            for genre in res['genres']:
                genres.append(genre['name'])
            return f"<b>Genres:</b> {', '.join(genres)}"
        elif res['themes']:
            for theme in res['themes']:
                themes.append(theme['name'])
            return f"<b>Themes:</b> {', '.join(themes)}"
        else:
            return "<i>No genres/themes information has been added to this title.</i>"

    async def anime_description(self) -> str:
        """
        Retrieve the description of the anime.

        Returns:
            str: The description if available, otherwise a message indicating no description is available.

        Example:
            parse_data.anime_description()
        """
        res = self.anime['data']
        if res['synopsis']:
            return f"<b>Description:</b> {res['synopsis']}"
        return "<i>No description information has been added to this title.</i>"

    async def anime_type(self) -> str:
        """
        Retrieve the type of the anime (e.g., TV, Movie).

        Returns:
            str: The type if available, otherwise a message indicating no type is available.

        Example:
            parse_data.anime_type()
        """
        res = self.anime['data']
        if res['type']:
            return f"<b>Type:</b> {res['type']}"
        else:
            return "<i>No type information has been added to this title.</i>"

    async def anime_episodes(self) -> str:
        """
        Retrieve the number of episodes of the anime.

        Returns:
            str: The number of episodes if available, otherwise a message indicating no episode information is available.

        Example:
            parse_data.anime_episodes()
        """
        res = self.anime['data']
        if res['episodes']:
            return f"<b>Episodes amount:</b> {res['episodes']}"
        else:
            return "<i>No episodes information has been added to this title.</i>"

    async def anime_status(self) -> str:
        """
        Retrieve the status of the anime (e.g., Airing, Finished).

        Returns:
            str: The status if available, otherwise a message indicating no status information is available.

        Example:
            parse_data.anime_status()
        """
        res = self.anime['data']
        if res['status']:
            return f"<b>Status:</b> {res['status']}"
        else:
            return "<i>No status information has been added to this title.</i>"


class ParseAnimeDataFromSearch:
    """
    A class for parsing anime data retrieved from the Jikan API.

    Attributes:
        anime (dict): The anime data to parse.
    """
    def __init__(
            self,
            anime_data
    ) -> None:
        """
        Initialize the ParseAnimeData with anime data.

        Args:
            anime_data (dict): The anime data to parse.

        Examples:
            parse_data = ParseAnimeDataFromSearch(anime_data)
        """
        self.anime = anime_data

    async def is_data(self):
        if self.anime != 'Not found':
            return False
        return True

    async def anime_image(self) -> str:
        """
        Retrieve the image URL of the anime.

        Returns:
            str: The image URL if available, otherwise a message indicating no image is available.

        Example:
            parse_data.anime_image()
        """
        res = self.anime['data'][0]
        if res['images']:
            if res['images']['jpg']['large_image_url']:
                return res['images']['jpg']['large_image_url']
        return 'Image has not been added to this title.'

    async def anime_title(self) -> str:
        """
        Retrieve the titles of the anime.

        Returns:
            str: A formatted string of the anime's titles.

        Example:
            parse_data.anime_title()
        """
        res = self.anime['data'][0]
        titles = []
        if res['title_english']:
            titles.append(res['title_english'])
        if res['title']:
            titles.append(res['title'])
        return ' / '.join(titles)

    async def anime_score(self) -> str | float:
        """
        Retrieve the score of the anime.

        Returns:
            str | float: The anime's score if available, otherwise a message indicating no score is available.

        Example:
            parse_data.anime_score()
        """
        res = self.anime['data'][0]
        if res['score']:
            return res['score']
        else:
            return "No score information has been added to this title."

    async def anime_year(self) -> str:
        """
        Retrieve the release year of the anime.

        Returns:
            str: The release year if available, otherwise a message indicating no year is available.

        Example:
            parse_data.anime_year()
        """
        res = self.anime['data'][0]
        if res['year']:
            return f"<b>Year:</b> {res['year']}"
        else:
            return "No year information has been added to this title."

    async def anime_included_genres_or_themes(self) -> str:
        """
        Retrieve the genres or themes of the anime.

        Returns:
            str: A formatted string of the anime's genres or themes if available,
            otherwise a message indicating no genres or themes are available.

        Example:
            parse_data.anime_included_genres_or_themes()
        """
        res = self.anime['data'][0]
        genres = []
        themes = []
        if res['genres']:
            for genre in res['genres']:
                genres.append(genre['name'])
                return f"<b>Genres:</b> {', '.join(genres)}"
        elif res['themes']:
            for theme in res['themes']:
                themes.append(theme['name'])
                return f"<b>Themes:</b> {', '.join(themes)}"
        else:
            return "No genres or themes information has been added to this title."

    async def anime_description(self) -> str:
        """
        Retrieve the description of the anime.

        Returns:
            str: The description if available, otherwise a message indicating no description is available.

        Example:
            parse_data.anime_description()
        """
        res = self.anime['data'][0]
        if res['synopsis']:
            return f"<b>Description:</b> {res['synopsis']}"
        return "No description information has been added to this title."

    async def anime_type(self) -> str:
        """
        Retrieve the type of the anime (e.g., TV, Movie).

        Returns:
            str: The type if available, otherwise a message indicating no type is available.

        Example:
            parse_data.anime_type()
        """
        res = self.anime['data'][0]
        if res['type']:
            return f"<b>Type:</b> {res['type']}"
        else:
            return "No type information has been added to this title."

    async def anime_episodes(self) -> str | int:
        """
        Retrieve the number of episodes of the anime.

        Returns:
            int | str: The number of episodes if available,
            otherwise a message indicating no episode information is available.

        Example:
            parse_data.anime_episodes()
        """
        res = self.anime['data'][0]
        if res['episodes']:
            return res['episodes']
        else:
            return "No episodes information has been added to this title."

    async def anime_status(self) -> str:
        """
        Retrieve the status of the anime (e.g., Airing, Finished).

        Returns:
            str: The status if available, otherwise a message indicating no status information is available.

        Example:
            parse_data.anime_status()
        """
        res = self.anime['data'][0]
        if res['status']:
            return res['status']
        else:
            return "No status information has been added to this title."
