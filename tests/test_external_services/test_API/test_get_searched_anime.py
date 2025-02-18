import urllib.parse

import pytest
from aioresponses import aioresponses
from Git.Anime_Bot.external_services.API import JikanAPI


anime = JikanAPI()
url = f'https://api.jikan.moe/v4/anime'


@pytest.mark.asyncio
async def test_get_searched_anime():

    with aioresponses() as mock:
        mock_response = {
            'pagination': {},
            'data': []
        }
        parameters = {'q': 'Oshi no ko'}
        encode_params = urllib.parse.urlencode(parameters)
        mock.get(f"{url}?{encode_params}", status=200, payload=mock_response)
        response = await anime.get_searched_anime(parameters)

        assert 'data' in response


@pytest.mark.asyncio
async def test_get_searched_anime_not_found():

    with aioresponses() as mock:
        parameters = {'letter': '1, 2, 3'}
        encode_params = urllib.parse.urlencode(parameters)
        mock.get(f"{url}?{encode_params}", status=400)
        response = await anime.get_searched_anime(parameters)

        assert response == 'Not found'
