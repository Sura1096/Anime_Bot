import pytest

from aioresponses import aioresponses

from Git.Anime_Bot.external_services.API import JikanAPI


anime = JikanAPI()
url = f'https://api.jikan.moe/v4/random/anime'


@pytest.mark.asyncio
async def test_get_random_anime():

    with aioresponses() as mock:
        mock_response = {
            'data': {}
        }
        mock.get(url, status=200, payload=mock_response)
        response = await anime.get_random_anime()

        assert 'data' in response


@pytest.mark.asyncio
async def test_get_random_anime_not_found():

    with aioresponses() as mock:
        mock.get(url, status=400)
        response = await anime.get_random_anime()

        assert response == 'Not found'
