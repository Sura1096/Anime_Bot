import pytest
import urllib.parse

from aioresponses import aioresponses

from Git.Anime_Bot.external_services.API import JikanAPI


anime = JikanAPI()
url = f'https://api.jikan.moe/v4/anime'


@pytest.mark.asyncio
async def test_search_by_genres_id():

    with aioresponses() as mock:
        mock_response = {
            'pagination': {},
            'data': [
                {
                    'genres': []
                }
            ]
        }
        parameters = {'genres': '1, 2, 3'}
        encode_params = urllib.parse.urlencode(parameters)
        mock.get(f"{url}?{encode_params}", status=200, payload=mock_response)
        response = await anime.search_by_genres_id(parameters)

        assert 'data' in response
        assert 'genres' in response['data'][0]


@pytest.mark.asyncio
async def test_search_by_genres_id_with_no_data():

    with aioresponses() as mock:
        mock_response = {
            'pagination': {},
            'data': []
        }
        parameters = {'genres': '1, 2, 3, 4, 5, 6'}
        encode_params = urllib.parse.urlencode(parameters)
        mock.get(f"{url}?{encode_params}", status=200, payload=mock_response)
        response = await anime.search_by_genres_id(parameters)

        assert 'data' in response
        assert not response['data']


@pytest.mark.asyncio
async def test_search_by_genres_id_not_found():

    with aioresponses() as mock:
        parameters = {'letter': '1, 2, 3'}
        encode_params = urllib.parse.urlencode(parameters)
        mock.get(f"{url}?{encode_params}", status=400)
        response = await anime.search_by_genres_id(parameters)

        assert response == 'Not found'
