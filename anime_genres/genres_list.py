from jikanpy import Jikan


def genres():
    anime = Jikan()
    data = anime.genres('anime')['data']
    genres_dict: dict[int, str] = {}

    for item in data:
        genres_dict[item['mal_id']] = item['name']

    return genres_dict
