import asyncio

from aiogram import Bot, Dispatcher

from config_data.config import load_config
from handlers import (
    genres_handlers,
    inline_mode_handlers,
    other_handlers,
    popular_anime_handlers,
    random_anime_handlers,
    user_handlers,
)
from keyboards.set_menu import set_main_menu


async def main() -> None:
    """
    Initializes and starts the Telegram bot.

    This function loads the configuration, sets up the bot and dispatcher,
    includes handlers, and starts polling for updates.
    """
    config = load_config('.env')
    bot_token = config.tg_bot.token
    bot = Bot(token=bot_token)
    dp = Dispatcher()
    await set_main_menu(bot)

    dp.include_router(user_handlers.router)
    dp.include_router(genres_handlers.router)
    dp.include_router(random_anime_handlers.router)
    dp.include_router(popular_anime_handlers.router)
    dp.include_router(inline_mode_handlers.router)
    dp.include_router(other_handlers.router)

    # Skip previous updates and start polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
