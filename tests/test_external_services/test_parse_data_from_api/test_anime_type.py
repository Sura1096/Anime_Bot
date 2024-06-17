import pytest

from Git.Anime_Bot.external_services.parse_data_from_api import ParseAnimeData, ParseAnimeDataFromSearch


# Tests for ParseAnimeData class
@pytest.mark.asyncio
async def test_anime_type_with_type():
    anime_data_with_type = {
        'data': {
            'type': 'TV'
        }
    }
    parser = ParseAnimeData(anime_data_with_type)
    anime_type = await parser.anime_type()
    assert anime_type == '<b>Type:</b> TV'


@pytest.mark.asyncio
async def test_anime_type_no_type():
    anime_data_no_type = {
        'data': {
            'type': None
        }
    }
    parser = ParseAnimeData(anime_data_no_type)
    anime_type = await parser.anime_type()
    assert anime_type == '<i>No type information has been added to this title.</i>'


# Tests for ParseAnimeDataFromSearch class
@pytest.mark.asyncio
async def test_anime_type():
    anime_data_with_type = {
        'data': [{
            'type': 'TV'
        }]
    }
    parser = ParseAnimeDataFromSearch(anime_data_with_type)
    anime_type = await parser.anime_type()
    assert anime_type == '<b>Type:</b> TV'


@pytest.mark.asyncio
async def test_anime_type_without_type():
    anime_data_without_type = {
        'data': [{
            'type': None
        }]
    }
    parser = ParseAnimeDataFromSearch(anime_data_without_type)
    anime_type = await parser.anime_type()
    assert anime_type == "No type information has been added to this title."
