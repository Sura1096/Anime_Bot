import pytest

from Git.Anime_Bot.external_services.parse_data_from_api import ParseAnimeData


@pytest.mark.asyncio
async def test_anime_description_with_synopsis():
    anime_data_with_synopsis = {
        'data': {
            'synopsis': 'A great story about heroes.'
        }
    }
    parser = ParseAnimeData(anime_data_with_synopsis)
    description = await parser.anime_description()
    assert description == '<b>Description:</b> A great story about heroes.'


@pytest.mark.asyncio
async def test_anime_description_no_synopsis():
    anime_data_no_synopsis = {
        'data': {
            'synopsis': None
        }
    }
    parser = ParseAnimeData(anime_data_no_synopsis)
    description = await parser.anime_description()
    assert description == '<i>No description information has been added to this title.</i>'
