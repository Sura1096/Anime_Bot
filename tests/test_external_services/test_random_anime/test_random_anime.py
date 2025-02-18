from unittest.mock import AsyncMock, patch

import pytest
from Git.Anime_Bot.external_services.random_anime import RandomAnime


@pytest.mark.asyncio
@patch('Git.Anime_Bot.external_services.random_anime.JikanAPI')
@patch('Git.Anime_Bot.external_services.random_anime.ParseAnimeData')
async def test_get_random_anime(mock_parse_anime_data, mock_jikan_api):
    # Мокаем данные, возвращаемые JikanAPI
    mock_jikan_api.return_value.get_random_anime = AsyncMock(return_value={
        'data': {
            'images': {
                'jpg': {
                    'image_url': 'https://example.com/image.jpg'
                }
            },
            'title_english': 'My Hero Academia',
            'title': 'Boku no Hero Academia',
            'score': 8.5,
            'year': 2020,
            'genres': [{'name': 'Action'}, {'name': 'Adventure'}],
            'themes': [{'name': 'Super Power'}, {'name': 'School'}],
            'synopsis': 'A great story about heroes.',
            'type': 'TV',
            'episodes': 24,
            'status': 'Finished Airing'
        }
    })

    # Мокаем методы класса ParseAnimeData
    mock_parse_anime_data.return_value.anime_image = AsyncMock(
        return_value='https://example.com/image.jpg'
    )
    mock_parse_anime_data.return_value.anime_title = AsyncMock(
        return_value='<b>Titles:</b> My Hero Academia / Boku no Hero Academia'
    )
    mock_parse_anime_data.return_value.anime_score = AsyncMock(
        return_value='<b>Score:</b> 8.5'
    )
    mock_parse_anime_data.return_value.anime_year = AsyncMock(
        return_value='<b>Year:</b> 2020'
    )
    mock_parse_anime_data.return_value.anime_included_genres_or_themes = AsyncMock(
        return_value='<b>Genres:</b> Action, Adventure'
    )
    mock_parse_anime_data.return_value.anime_description = AsyncMock(
        return_value='<b>Description:</b> A great story about heroes.'
    )
    mock_parse_anime_data.return_value.anime_type = AsyncMock(
        return_value='<b>Type:</b> TV'
    )
    mock_parse_anime_data.return_value.anime_episodes = AsyncMock(
        return_value='<b>Episodes amount:</b> 24'
    )
    mock_parse_anime_data.return_value.anime_status = AsyncMock(
        return_value='<b>Status:</b> Finished Airing'
    )

    random_anime = await RandomAnime.get_random_anime()

    assert random_anime == (
        'https://example.com/image.jpg',
        '<b>Titles:</b> My Hero Academia / Boku no Hero Academia',
        '<b>Score:</b> 8.5',
        '<b>Year:</b> 2020',
        '<b>Genres:</b> Action, Adventure',
        '<b>Description:</b> A great story about heroes.',
        '<b>Type:</b> TV',
        '<b>Episodes amount:</b> 24',
        '<b>Status:</b> Finished Airing'
    )


@pytest.mark.asyncio
async def test_random_anime():
    anime_info = (
        'https://example.com/image.jpg',
        'My Hero Academia / Boku no Hero Academia',
        '8.5',
        '<b>Year:</b> 2020',
        '<b>Genres:</b> Action, Adventure',
        '<b>Description:</b> A great story about heroes.',
        '<b>Type:</b> TV',
        '24',
        'Finished Airing'
    )

    expected_dict = {
        'image': 'https://example.com/image.jpg',
        'title': 'My Hero Academia / Boku no Hero Academia',
        'score': '8.5',
        'year': '<b>Year:</b> 2020',
        'genres': '<b>Genres:</b> Action, Adventure',
        'desc': '<b>Description:</b> A great story about heroes.',
        'type_anime': '<b>Type:</b> TV',
        'eps': '24',
        'status': 'Finished Airing'
    }

    random_anime_dict = await RandomAnime.random_anime(anime_info)
    assert random_anime_dict == expected_dict
