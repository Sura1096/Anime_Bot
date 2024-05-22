from anime_genres.genres_list import genres
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from jikanpy import Jikan


def user_choice_buttons():
    keyboard_builder = InlineKeyboardBuilder()
    category_buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text='Genres 📁',
                             callback_data='genres'),
        InlineKeyboardButton(text='Random anime 🃏',
                             callback_data='random anime'),
        InlineKeyboardButton(text='Popular anime 🔥',
                             callback_data='popular anime'),
        InlineKeyboardButton(text='Search by name 🔎',
                             switch_inline_query_current_chat='')
    ]

    keyboard_builder.row(*category_buttons, width=1)
    return keyboard_builder


def help_command_button():
    admin_link = InlineKeyboardButton(text='Contact admin',
                                      url='https://t.me/Sura_1096')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[admin_link]])
    return keyboard


def genres_buttons():
    buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text=f'🔴 {genres[genre_id]}', callback_data='🔴_' + str(genre_id)) for genre_id in genres
    ]
    return buttons


def edit_genres_buttons(selected_genres):
    buttons = []
    for genre_id, genre_name in genres.items():
        if genre_id in selected_genres:
            buttons.append(InlineKeyboardButton(text=f'🟢 {genre_name}', callback_data=f'🟢_{genre_id}'))
        else:
            buttons.append(InlineKeyboardButton(text=f'🔴 {genre_name}', callback_data=f'🔴_{genre_id}'))
    return buttons


def apply_filter_for_genres_button():
    apply_filter: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text='Apply filter 🟢', callback_data='apply filter for genres')
    ]
    return apply_filter


def end_home_button():
    home_button: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text='To home page ⛩', callback_data='home page')
    ]
    return home_button


def random_home_buttons():
    keyboard_builder = InlineKeyboardBuilder()
    home_random_buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text='Next 🟢', callback_data='random anime'),
        InlineKeyboardButton(text='To home page ⛩', callback_data='home page')
    ]
    keyboard_builder.row(*home_random_buttons, width=1)
    return keyboard_builder


def popular_anime_buttons():
    anime = Jikan()
    data = anime.top('anime')
    buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text=f'⛩ {item["title"]}',
                             switch_inline_query_current_chat=f'{item["title"]}') for item in data['data']
    ]
    return buttons
