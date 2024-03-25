import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import load_config
from handlers import user_handlers, other_handlers
from keyboards.set_menu import set_main_menu


async def main() -> None:
    config = load_config('.env')
    bot_token = config.tg_bot.token
    bot = Bot(token=bot_token)
    dp = Dispatcher()
    await set_main_menu(bot)

    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Skip previous updates and start polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())