import pytest

from Git.Anime_Bot.external_services.parse_data_from_api import ParseAnimeData


@pytest.mark.asyncio
async def test_anime_episodes_with_episodes():
    anime_data_with_episodes = {
        'data': {
            'episodes': 24
        }
    }
    parser = ParseAnimeData(anime_data_with_episodes)
    episodes = await parser.anime_episodes()
    assert episodes == '<b>Episodes amount:</b> 24'


@pytest.mark.asyncio
async def test_anime_episodes_no_episodes():
    anime_data_no_episodes = {
        'data': {
            'episodes': None
        }
    }
    parser = ParseAnimeData(anime_data_no_episodes)
    episodes = await parser.anime_episodes()
    assert episodes == '<i>No episodes information has been added to this title.</i>'
