class ParseAnimeData:
    '''
    TODO:
    Handle situation when there is no anime data from API
    '''
    def anime_image(self, anime_data):
        res = anime_data['data']
        if res['images']:
            if res['images']['jpg']['image_url']:
                return res['images']['jpg']['image_url']
            elif res['images']['webp']['image_url']:
                return res['images']['webp']['image_url']
        return 'There is no image info.'

    def anime_title(self, anime_data):
        res = anime_data['data']
        titles = []
        if res['title_english']:
            titles.append(res['title_english'])
        if res['title']:
            titles.append(res['title'])
        return f"Titles: {' / '.join(titles)}"

    def anime_score(self, anime_data):
        res = anime_data['data']
        if res['score']:
            return f"Score: {res['score']}"
        else:
            return None

    def anime_year(self, anime_data):
        res = anime_data['data']
        if res['year']:
            return f"Year: {res['year']}"
        else:
            return None

    def anime_included_genres_or_themes(self, anime_data):
        res = anime_data['data']
        genres = []
        themes = []
        if res['genres']:
            for genre in res['genres']:
                genres.append(genre['name'])
                return f"Genres: {', '.join(genres)}"
        elif res['themes']:
            for theme in res['themes']:
                themes.append(theme['name'])
                return f"Themes: {', '.join(themes)}"
        else:
            return None

    def anime_description(self, anime_data):
        res = anime_data['data']
        if res['synopsis']:
            return f"Description: {res['synopsis']}"
        return None