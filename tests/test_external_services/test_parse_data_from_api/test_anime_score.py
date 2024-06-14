import pytest

from Git.Anime_Bot.external_services.parse_data_from_api import ParseAnimeData, ParseAnimeDataFromSearch


# Tests for ParseAnimeData class
@pytest.mark.asyncio
async def test_anime_score_with_score():
    anime_data_with_score = {
        'data': {
            'score': 8.5
        }
    }
    parser = ParseAnimeData(anime_data_with_score)
    score = await parser.anime_score()
    assert score == '<b>Score:</b> 8.5'


@pytest.mark.asyncio
async def test_anime_score_no_score():
    anime_data_no_score = {
        'data': {
            'score': None
        }
    }
    parser = ParseAnimeData(anime_data_no_score)
    score = await parser.anime_score()
    assert score == '<i>No score information has been added to this title.</i>'


# Tests for ParseAnimeDataFromSearch class
@pytest.mark.asyncio
async def test_anime_score():
    anime_data_with_score = {
        'data': [{
            'score': 8.5
        }]
    }
    parser = ParseAnimeDataFromSearch(anime_data_with_score)
    score = await parser.anime_score()
    assert score == 8.5


@pytest.mark.asyncio
async def test_anime_score_without_score():
    anime_data_without_score = {
        'data': [{
            'score': None
        }]
    }
    parser = ParseAnimeDataFromSearch(anime_data_without_score)
    score = await parser.anime_score()
    assert score == "No score information has been added to this title."
