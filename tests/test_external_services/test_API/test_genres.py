import pytest
from aioresponses import aioresponses
from Git.Anime_Bot.external_services.API import JikanAPI


anime = JikanAPI()
url = f'https://api.jikan.moe/v4/genres/anime'


@pytest.mark.asyncio
async def test_genres():

    with aioresponses() as mock:
        mock_response = {
            'data': [
                {
                    'mal_id': 1,
                    'name': 'Action'
                }
            ]
        }
        mock.get(url, status=200, payload=mock_response)
        response = await anime.genres()

        assert 'data' in response
        assert 'name' in response['data'][0]


@pytest.mark.asyncio
async def test_genres_not_found():

    with aioresponses() as mock:
        mock.get(url, status=404)
        response = await anime.genres()

        assert response == 'Not found'
