import pytest

from aioresponses import aioresponses

from Git.Anime_Bot.external_services.API import JikanAPI


anime = JikanAPI()


def url(anime_id):
    return f'https://api.jikan.moe/v4/anime/{anime_id}'


@pytest.mark.asyncio
async def test_get_anime_by_id():
    jikan_api = JikanAPI()

    anime_id = 5
    api_url = f'https://api.jikan.moe/v4/anime/{anime_id}'

    expected_response = {
        'data': {
            'mal_id': 5,
            'url': 'https://myanimelist.net/anime/5/Cowboy_Bebop__Tengoku_no_Tobira',
            'images': {
                'jpg': {
                    'image_url': 'https://cdn.myanimelist.net/images/anime/1439/93480.jpg',
                    'small_image_url': 'https://cdn.myanimelist.net/images/anime/1439/93480t.jpg',
                    'large_image_url': 'https://cdn.myanimelist.net/images/anime/1439/93480l.jpg'
                },
                'webp': {
                    'image_url': 'https://cdn.myanimelist.net/images/anime/1439/93480.webp',
                    'small_image_url': 'https://cdn.myanimelist.net/images/anime/1439/93480t.webp',
                    'large_image_url': 'https://cdn.myanimelist.net/images/anime/1439/93480l.webp'
                }
            },
            'trailer': {
                'youtube_id': None,
                'url': None,
                'embed_url': None,
                'images': {
                    'image_url': None,
                    'small_image_url': None,
                    'medium_image_url': None,
                    'large_image_url': None,
                    'maximum_image_url': None
                }
            },
            'approved': True,
            'titles': [
                {
                    'type': 'Default',
                    'title': 'Cowboy Bebop: Tengoku no Tobira'
                },
                {
                    'type': 'Synonym',
                    'title': "Cowboy Bebop: Knockin' on Heaven's Door"
                },
                {
                    'type': 'Japanese',
                    'title': 'カウボーイビバップ 天国の扉'
                },
                {
                    'type': 'English',
                    'title': 'Cowboy Bebop: The Movie'
                },
                {
                    'type': 'German',
                    'title': 'Cowboy Bebop: Der Film'
                },
                {
                    'type': 'Spanish',
                    'title': 'Cowboy Bebop: La Película'
                },
                {
                    'type': 'French',
                    'title': 'Cowboy Bebop: Le Film'
                }
            ],
            'title': 'Cowboy Bebop: Tengoku no Tobira',
            'title_english': 'Cowboy Bebop: The Movie',
            'title_japanese': 'カウボーイビバップ 天国の扉',
            'title_synonyms': [
                "Cowboy Bebop: Knockin' on Heaven's Door"
            ],
            'type': 'Movie',
            'source': 'Original',
            'episodes': 1,
            'status': 'Finished Airing',
            'airing': False,
            'aired': {
                'from': '2001-09-01T00:00:00+00:00',
                'to': None,
                'prop': {
                    'from': {
                        'day': 1,
                        'month': 9,
                        'year': 2001
                    },
                    'to': {
                        'day': None,
                        'month': None,
                        'year': None
                    }
                },
                'string': 'Sep 1, 2001'
            },
            'duration': '1 hr 55 min',
            'rating': 'R - 17+ (violence & profanity)',
            'score': 8.38,
            'scored_by': 216553,
            'rank': 199,
            'popularity': 619,
            'members': 380333,
            'favorites': 1597,
            'synopsis': 'Another day, another bounty—such is the life of the often unlucky crew of the Bebop. '
                        'However, this routine is interrupted when Faye, who is chasing a fairly worthless '
                        'target on Mars, witnesses an oil tanker suddenly explode, causing mass hysteria. '
                        'As casualties mount due to a strange disease spreading through the smoke from the blast,'
                        ' a whopping three hundred million woolong price is placed on the head of the '
                        'supposed perpetrator.\n\nWith lives at stake and a solution to their money problems '
                        'in sight, the Bebop crew springs into action. Spike, Jet, Faye, and Edward, '
                        'followed closely by Ein, split up to pursue different leads across Alba City. '
                        'Through their individual investigations, they discover a cover-up scheme involving '
                        'a pharmaceutical company, revealing a plot that reaches much further than the '
                        'ragtag team of bounty hunters could have realized.\n\n[Written by MAL Rewrite]',
            'background': '',
            'season': None,
            'year': None,
            'broadcast': {
                'day': None,
                'time': None,
                'timezone': None,
                'string': None
            },
            'producers': [
                {
                    'mal_id': 14,
                    'type': 'anime',
                    'name': 'Sunrise',
                    'url': 'https://myanimelist.net/anime/producer/14/Sunrise'
                },
                {
                    'mal_id': 23,
                    'type': 'anime',
                    'name': 'Bandai Visual',
                    'url': 'https://myanimelist.net/anime/producer/23/Bandai_Visual'
                }
            ],
            'licensors': [
                {
                    'mal_id': 15,
                    'type': 'anime',
                    'name': 'Sony Pictures Entertainment',
                    'url': 'https://myanimelist.net/anime/producer/15/Sony_Pictures_Entertainment'
                },
                {
                    'mal_id': 102,
                    'type': 'anime',
                    'name': 'Funimation',
                    'url': 'https://myanimelist.net/anime/producer/102/Funimation'
                }
            ],
            'studios': [
                {
                    'mal_id': 4,
                    'type': 'anime',
                    'name': 'Bones',
                    'url': 'https://myanimelist.net/anime/producer/4/Bones'
                }
            ],
            'genres': [
                {
                    'mal_id': 1,
                    'type': 'anime',
                    'name': 'Action',
                    'url': 'https://myanimelist.net/anime/genre/1/Action'
                },
                {
                    'mal_id': 24,
                    'type': 'anime',
                    'name': 'Sci-Fi',
                    'url': 'https://myanimelist.net/anime/genre/24/Sci-Fi'
                }
            ],
            'explicit_genres': [],
            'themes': [
                {
                    'mal_id': 50,
                    'type': 'anime',
                    'name': 'Adult Cast',
                    'url': 'https://myanimelist.net/anime/genre/50/Adult_Cast'
                },
                {
                    'mal_id': 29,
                    'type': 'anime',
                    'name': 'Space',
                    'url': 'https://myanimelist.net/anime/genre/29/Space'
                }
            ],
            'demographics': []
        }
    }

    with aioresponses() as m:
        m.get(api_url, payload=expected_response)

        response = await jikan_api.get_anime_by_id(anime_id)
        assert response == expected_response


@pytest.mark.asyncio
async def test_get_anime_by_id_not_found():
    jikan_api = JikanAPI()

    anime_id = 2
    api_url = f'https://api.jikan.moe/v4/anime/{anime_id}'

    with aioresponses() as m:
        m.get(api_url)

        response = await jikan_api.get_anime_by_id(anime_id)
        assert response == None
