import pytest

from aioresponses import aioresponses

from Git.Anime_Bot.external_services.API import JikanAPI


anime = JikanAPI()


def url(anime_id):
    return f'https://api.jikan.moe/v4/anime/{anime_id}'


@pytest.mark.asyncio
async def test_get_anime_by_id():

    with aioresponses() as mock:
        mock_response = {
            'data':
                {
                    'mal_id': 5
                }
        }
        mock.get(url(5), status=200, payload=mock_response)

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
