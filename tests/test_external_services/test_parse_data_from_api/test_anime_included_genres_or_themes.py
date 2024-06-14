import pytest

from Git.Anime_Bot.external_services.parse_data_from_api import ParseAnimeData, ParseAnimeDataFromSearch


# Tests for ParseAnimeData class
@pytest.mark.asyncio
async def test_anime_included_genres_or_themes_with_genres():
    anime_data_with_genres = {
        'data': {
            'genres': [{'name': 'Action'}, {'name': 'Adventure'}],
            'themes': None
        }
    }
    parser = ParseAnimeData(anime_data_with_genres)
    genres_or_themes = await parser.anime_included_genres_or_themes()
    assert genres_or_themes == '<b>Genres:</b> Action, Adventure'


@pytest.mark.asyncio
async def test_anime_included_genres_or_themes_with_themes():
    anime_data_with_themes = {
        'data': {
            'genres': None,
            'themes': [{'name': 'Super Power'}, {'name': 'School'}]
        }
    }
    parser = ParseAnimeData(anime_data_with_themes)
    genres_or_themes = await parser.anime_included_genres_or_themes()
    assert genres_or_themes == '<b>Themes:</b> Super Power, School'


@pytest.mark.asyncio
async def test_anime_included_genres_or_themes_no_genres_or_themes():
    anime_data_no_genres_or_themes = {
        'data': {
            'genres': None,
            'themes': None
        }
    }
    parser = ParseAnimeData(anime_data_no_genres_or_themes)
    genres_or_themes = await parser.anime_included_genres_or_themes()
    assert genres_or_themes == '<i>No genres/themes information has been added to this title.</i>'


# Tests for ParseAnimeDataFromSearch class
@pytest.mark.asyncio
async def test_anime_included_genres_or_themes():
    anime_data_with_genres = {
        'data': [{
            'genres': [{'name': 'Action'}, {'name': 'Adventure'}],
            'themes': None
        }]
    }
    parser = ParseAnimeDataFromSearch(anime_data_with_genres)
    genres_or_themes = await parser.anime_included_genres_or_themes()
    assert genres_or_themes == '<b>Genres:</b> Action, Adventure'


@pytest.mark.asyncio
async def test_anime_included_themes():
    anime_data_with_themes = {
        'data': [{
            'genres': None,
            'themes': [{'name': 'Super Power'}, {'name': 'School'}]
        }]
    }
    parser = ParseAnimeDataFromSearch(anime_data_with_themes)
    genres_or_themes = await parser.anime_included_genres_or_themes()
    assert genres_or_themes == '<b>Themes:</b> Super Power, School'


@pytest.mark.asyncio
async def test_anime_included_genres_empty():
    anime_data_no_genres_or_themes = {
        'data': [{
            'genres': None,
            'themes': None
        }]
    }
    parser = ParseAnimeDataFromSearch(anime_data_no_genres_or_themes)
    genres_or_themes = await parser.anime_included_genres_or_themes()
    assert genres_or_themes == "No genres or themes information has been added to this title."
