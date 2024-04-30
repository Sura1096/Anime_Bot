class ParseAnimeData:
    '''
    TODO:
    Handle situation when there is no anime data from API
    '''

    def __init__(self, anime_data='Not found'):
        self.anime = anime_data

    def anime_image(self):
        res = self.anime['data']
        if res['images']:
            if res['images']['jpg']['image_url']:
                return res['images']['jpg']['image_url']
            elif res['images']['webp']['image_url']:
                return res['images']['webp']['image_url']
        return '<i>There is no image info.</i>'

    def anime_title(self):
        res = self.anime['data']
        titles = []
        if res['title_english']:
            titles.append(res['title_english'])
        if res['title']:
            titles.append(res['title'])
        return f"<b>Titles:</b> {' / '.join(titles)}"

    def anime_score(self):
        res = self.anime['data']
        if res['score']:
            return f"<b>Score:</b> {res['score']}"
        else:
            return None

    def anime_year(self):
        res = self.anime['data']
        if res['year']:
            return f"<b>Year:</b> {res['year']}"
        else:
            return "<i>There is no year info.</i>"

    def anime_included_genres_or_themes(self):
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
            return None

    def anime_description(self):
        res = self.anime['data']
        if res['synopsis']:
            return f"<b>Description:</b> {res['synopsis']}"
        return None

    def anime_type(self):
        res = self.anime['data']
        if res['type']:
            return f"<b>Type:</b> {res['type']}"
        else:
            return "<i>No type information has been added to this title.</i>"

    def anime_episodes(self):
        res = self.anime['data']
        if res['episodes']:
            return f"<b>Episodes amount:</b> {res['episodes']}"
        else:
            return "<i>No episodes information has been added to this title.</i>"

    def anime_status(self):
        res = self.anime['data']
        if res['status']:
            return f"<b>Status:</b> {res['status']}"
        else:
            return "<i>No status information has been added to this title.</i>"