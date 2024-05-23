from API import JikanAPI
from parse_data_from_api import ParseAnimeData


def get_random_anime():
    anime = JikanAPI()
    data = anime.get_random_anime()
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
