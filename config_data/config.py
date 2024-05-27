from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    """
    Dataclass for storing Telegram bot configuration.

    Attributes:
        token (str): The token used to authenticate the bot with the Telegram API.
    """
    token: str  # Bot token


@dataclass
class Config:
    """
    Dataclass for storing the configuration of the application.

    Attributes:
        tg_bot (TgBot): An instance of the TgBot dataclass containing the bot's configuration.
    """
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN')
        )
    )
