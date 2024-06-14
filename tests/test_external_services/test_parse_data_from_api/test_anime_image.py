import pytest

from Git.Anime_Bot.external_services.parse_data_from_api import ParseAnimeData


@pytest.mark.asyncio
async def test_anime_image_with_image():
    anime_data_with_image = {
        'data': {
            'images': {
                'jpg': {
                    'image_url': 'https://example.com/image.jpg'
                }
            }
        }
    }

    parser = ParseAnimeData(anime_data_with_image)
    image_url = await parser.anime_image()
    assert image_url == 'https://example.com/image.jpg'


@pytest.mark.asyncio
async def test_anime_image_without_image():
    anime_data_without_image = {
        'data': {
            'images': {
                'jpg': {
                    'image_url': None
                }
            }
        }
    }

    parser = ParseAnimeData(anime_data_without_image)
    image_url = await parser.anime_image()
    assert image_url == '<i>Image has not been added to this title.</i>'


@pytest.mark.asyncio
async def test_anime_image_no_image_field():
    anime_data_no_image_field = {
        'data': {}
    }

    parser = ParseAnimeData(anime_data_no_image_field)
    image_url = await parser.anime_image()
    assert image_url == '<i>Image has not been added to this title.</i>'
