import pytest

from Git.Anime_Bot.external_services.parse_data_from_api import ParseAnimeData


@pytest.mark.asyncio
async def test_anime_title_both_titles():
    anime_data_with_both_titles = {
        'data': {
            'title_english': 'My Hero Academia',
            'title': 'Boku no Hero Academia'
        }
    }

    parser = ParseAnimeData(anime_data_with_both_titles)
    titles = await parser.anime_title()
    assert titles == '<b>Titles:</b> My Hero Academia / Boku no Hero Academia'


@pytest.mark.asyncio
async def test_anime_title_only_english():
    anime_data_with_english_title = {
        'data': {
            'title_english': 'My Hero Academia',
            'title': None
        }
    }

    parser = ParseAnimeData(anime_data_with_english_title)
    titles = await parser.anime_title()
    assert titles == '<b>Titles:</b> My Hero Academia'


@pytest.mark.asyncio
async def test_anime_title_only_original():
    anime_data_with_original_title = {
        'data': {
            'title_english': None,
            'title': 'Boku no Hero Academia'
        }
    }

    parser = ParseAnimeData(anime_data_with_original_title)
    titles = await parser.anime_title()
    assert titles == '<b>Titles:</b> Boku no Hero Academia'
