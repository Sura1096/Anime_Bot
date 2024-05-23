from dataclasses import dataclass
from environs import Env


@dataclass
class DatabaseConfig:
    database: str  # Database
    db_host: str  # Database URL
    db_user: str  # Database Username
    db_password: str  # Database password


@dataclass
class TgBot:
    token: str  # Bot token


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN')
        )
    )
