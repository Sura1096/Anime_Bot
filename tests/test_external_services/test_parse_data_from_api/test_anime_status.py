import pytest
from Git.Anime_Bot.external_services.parse_data_from_api import ParseAnimeData
from Git.Anime_Bot.external_services.parse_searched_anime import ParseSearchedAnime


# Tests for ParseAnimeData class
@pytest.mark.asyncio
async def test_anime_status_with_status():
    anime_data_with_status = {
        'data': {
            'status': 'Finished Airing'
        }
    }
    parser = ParseAnimeData(anime_data_with_status)
    status = await parser.anime_status()
    assert status == '<b>Status:</b> Finished Airing'


@pytest.mark.asyncio
async def test_anime_status_no_status():
    anime_data_no_status = {
        'data': {
            'status': None
        }
    }
    parser = ParseAnimeData(anime_data_no_status)
    status = await parser.anime_status()
    assert status == '<i>No status information has been added to this title.</i>'


# Tests for ParseAnimeDataFromSearch class
@pytest.mark.asyncio
async def test_anime_status():
    anime_data_with_status = {
        'data': [{
            'status': 'Finished Airing'
        }]
    }
    parser = ParseSearchedAnime(anime_data_with_status)
    status = await parser.anime_status()
    assert status == 'Finished Airing'


@pytest.mark.asyncio
async def test_anime_status_without_status():
    anime_data_without_status = {
        'data': [{
            'status': None
        }]
    }
    parser = ParseSearchedAnime(anime_data_without_status)
    status = await parser.anime_status()
    assert status == "No status information has been added to this title."
