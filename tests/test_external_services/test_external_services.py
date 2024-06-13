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

        response = await anime.get_anime_by_id(5)

        assert 'data' in response
        assert 'mal_id' in response['data']


@pytest.mark.asyncio
async def test_get_anime_by_id_not_found():

    with aioresponses() as mock:
        mock.get(url(2), status=404)

        response = await anime.get_anime_by_id(2)
        assert response == 'Not found'
