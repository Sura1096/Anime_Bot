from aiogram import Bot
from aiogram.types import BotCommand
from lexicon.lexicon_menu_commands import LEXICON


async def set_main_menu(bot: Bot) -> None:
    """
    Set the main menu commands for the bot using the provided lexicon.

    This function takes a Bot instance and sets its main menu commands based
    on the command-description pairs defined in the LEXICON dictionary.

    Args:
        bot (Bot): The instance of the bot for which to set the main menu commands.
    """
    main_menu_commands = [
        BotCommand(
            command=command,
            description=description
        ) for command, description in LEXICON.items()
    ]
    await bot.set_my_commands(main_menu_commands)
