import requests


class JikanAPI:
    def __init__(self, base_url='https://api.jikan.moe/v4'):
        self.base_url = base_url

    def get_anime_by_id(self, anime_id: int):
        res = requests.get(f'{self.base_url}/anime/{anime_id}')
        if res.status_code != 200:
            return 'Not found'
        return res.json()

    def genres(self):
        res = requests.get(f'{self.base_url}/genres/anime')
        if res.status_code != 200:
            return 'Not found'
        genres = {}
        for genre in res.json()['data']:
            ind = genre['mal_id']
            genre_name = genre['name']
            genres[ind] = genre_name
        return genres

    def search_by_genres_id(self, params):
        '''
        params argument must be dictionary because it is a query parameter
        params = {
            "genres": "1,2,3" Replace with users parameters
        }
        '''
        full_url = f'{self.base_url}/anime'
        res = requests.get(full_url, params=params)
        if res.status_code != 200:
            return 'Not found'
        return res.json()

    def get_random_anime(self):
        res = requests.get(f'{self.base_url}/random/anime')
        if res.status_code != 200:
            return 'Not found'
        return res.json()