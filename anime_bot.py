from environs import Env
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

env = Env()
env.read_env()

bot_token = env('BOT_TOKEN')
bot = Bot(token=bot_token)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет, мой дорогой друг!'
                         '\nЯ аниме-бот, который готов помочь тебе с выбором аниме 🌟')


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Обратись к админу по ссылке https://t.me/Sura_1096, если у тебя по данному боту возникли:'
                         '\n1. Вопросы ❓'
                         '\n2. Жалобы 💢'
                         '\n3. Пожелания 🔆')


@dp.message()
async def rest_message_handler(message: Message):
    await message.answer('Извини, но в логику данного бота не заложена команда, которую ты отправил 👀')


if __name__ == '__main__':
    dp.run_polling(bot)