import pytest
from unittest.mock import patch, MagicMock
from Git.Anime_Bot.anime_genres.genres_list import genres


@pytest.mark.asyncio
@patch('Git.Anime_Bot.anime_genres.genres_list.Jikan')
async def test_genres(mock_jikan):
    mock_jikan.return_value.genres = MagicMock(return_value={
        'data': [
            {'mal_id': 1, 'name': 'Action'},
            {'mal_id': 2, 'name': 'Adventure'},
            {'mal_id': 3, 'name': 'Comedy'}
        ]
    })

    expected_result = {
        1: 'Action',
        2: 'Adventure',
        3: 'Comedy'
    }

    result = await genres()
    assert result == expected_result
