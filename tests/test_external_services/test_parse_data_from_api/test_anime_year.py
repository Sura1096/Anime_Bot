import pytest

from Git.Anime_Bot.external_services.parse_data_from_api import ParseAnimeData, ParseAnimeDataFromSearch


# Tests for ParseAnimeData class
@pytest.mark.asyncio
async def test_anime_year_with_year():
    anime_data_with_year = {
        'data': {
            'year': 2020
        }
    }
    parser = ParseAnimeData(anime_data_with_year)
    year = await parser.anime_year()
    assert year == '<b>Year:</b> 2020'


@pytest.mark.asyncio
async def test_anime_year_no_year():
    anime_data_no_year = {
        'data': {
            'year': None
        }
    }
    parser = ParseAnimeData(anime_data_no_year)
    year = await parser.anime_year()
    assert year == '<i>No year information has been added to this title.</i>'


# Tests for ParseAnimeDataFromSearch class
@pytest.mark.asyncio
async def test_anime_year():
    anime_data_with_year = {
        'data': [{
            'year': 2020
        }]
    }
    parser = ParseAnimeDataFromSearch(anime_data_with_year)
    year = await parser.anime_year()
    assert year == "<b>Year:</b> 2020"


@pytest.mark.asyncio
async def test_anime_year_without_year():
    anime_data_without_year = {
        'data': [{
            'year': None
        }]
    }
    parser = ParseAnimeDataFromSearch(anime_data_without_year)
    year = await parser.anime_year()
    assert year == "No year information has been added to this title."
