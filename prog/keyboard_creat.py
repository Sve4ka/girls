#  здесь находиться супер много функций для создения клавиатур

# TODO несколько страниц предметов, если предметов больше 8

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from db.db import get_all_my_shop, get_all_my_product, get_shop_product

def buy_product():  # TODO
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = InlineKeyboardButton("return", callback_data="buyer")
    keyboard.add(button)
    return keyboard


def eat_product():  # TODO
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = InlineKeyboardButton("return", callback_data="buyer")
    keyboard.add(button)
    return keyboard


def start_kb():  # TODO
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = InlineKeyboardButton(text="покупатель", callback_data="buyer")  #
    button2 = InlineKeyboardButton(text="продавец", callback_data="seller")  #
    button3 = InlineKeyboardButton(text="профиль", callback_data="profile")  #
    keyboard.add(button1, button2).add(button3)
    return keyboard


def buyer_kb():  # TODO
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = InlineKeyboardButton(text="home", callback_data="start")
    button2 = InlineKeyboardButton(text="profile", callback_data="profile_buyer")
    button3 = InlineKeyboardButton(text="buy product", callback_data="buy_product")
    button4 = InlineKeyboardButton(text="eat product", callback_data="eat_product")
    keyboard.add(button1, button2).add(button3).add(button4)
    return keyboard


def seller_kb():  # TODO
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = InlineKeyboardButton(text="home", callback_data="start")
    button2 = InlineKeyboardButton(text="profile", callback_data="profile_seller")
    button3 = InlineKeyboardButton(text="create product", callback_data="create_product")
    button4 = InlineKeyboardButton(text="my product", callback_data="my_product")
    button5 = InlineKeyboardButton(text="create shop", callback_data="create_shop")
    button6 = InlineKeyboardButton(text="my shop", callback_data="my_shop")
    keyboard.add(button1, button2).add(button3, button4).add(button5, button6)
    return keyboard


def profile_kb():  # TODO
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = InlineKeyboardButton(text="home", callback_data="start")
    keyboard.add(button1)
    return keyboard


def profile_buyer_kb():  # TODO
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = InlineKeyboardButton(text="return", callback_data="buyer")
    keyboard.add(button1)
    return keyboard


def profile_seller_kb():  # TODO
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = InlineKeyboardButton(text="return", callback_data="seller")
    keyboard.add(button1)
    return keyboard


def create_product_kb():  # TODO
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = InlineKeyboardButton(text="name", callback_data="name_product")
    button2 = InlineKeyboardButton(text="price", callback_data="price_product")
    button3 = InlineKeyboardButton(text="count", callback_data="count_product")
    button4 = InlineKeyboardButton(text="description", callback_data="description_product")
    button5 = InlineKeyboardButton(text="fruit(tap to vegetable)", callback_data="vegetable_product")
    button6 = InlineKeyboardButton(text="cancel", callback_data="cancel_product")
    keyboard.add(button1).add(button2).add(button3).add(button4).add(button5).add(button6)
    return keyboard


def create_shop_kb():  # TODO
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = InlineKeyboardButton(text="name", callback_data="name_shop")
    button2 = InlineKeyboardButton(text="decriprion", callback_data="decriprion_shop")
    button3 = InlineKeyboardButton(text="photo", callback_data="photo_shop")
    button4 = InlineKeyboardButton(text="cancel", callback_data="cancel_shop")
    keyboard.add(button1).add(button2).add(button3).add(button4)
    return keyboard


def my_shop_kb(user_id):  # TODO
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    for elem in get_all_my_shop(user_id):
        keyboard.add(InlineKeyboardButton(text=elem, callback_data="shop_"+elem))
    button4 = InlineKeyboardButton(text="return", callback_data="seller")
    keyboard.add(button4)
    return keyboard


def my_product_kb(user_id):  # TODO
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    for elem in get_all_my_product(user_id):
        keyboard.add(InlineKeyboardButton(text=elem, callback_data="product_"+elem))
    button5 = InlineKeyboardButton(text="return", callback_data="seller")
    keyboard.add(button5)
    return keyboard


def product_kb(user_id):  # TODO
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button6 = InlineKeyboardButton(text="return", callback_data="my_product")
    keyboard.add(button6)
    return keyboard


def shop_kb():  # TODO
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = InlineKeyboardButton(text="add product", callback_data="add_my_product")
    button2 = InlineKeyboardButton(text="product in shop", callback_data="product_shop")
    button3 = InlineKeyboardButton(text="statistic", callback_data="stats_shop")
    button4 = InlineKeyboardButton(text="return", callback_data="my_shop")
    keyboard.add(button1).add(button2).add(button3).add(button4)
    return keyboard


def add_my_product_kb(user_id):  # TODO
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    for elem in get_all_my_product(user_id):
        keyboard.add(InlineKeyboardButton(text=elem, callback_data="product_"+elem))
    button5 = InlineKeyboardButton(text="cancel", callback_data="shop")
    keyboard.add(button5)
    return keyboard


def product_shop_kb(user_id):  # TODO
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    shop_id = 0
    for elem in get_shop_product(user_id, shop_id):
        keyboard.add(InlineKeyboardButton(text=elem, callback_data="product_"+elem))
    button5 = InlineKeyboardButton(text="cancel", callback_data="shop")
    keyboard.add(button5)
    return keyboard


def stats_shop_kb(user_id):  # TODO
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = InlineKeyboardButton(text="return", callback_data="shop")
    keyboard.add(button1)
    return keyboard
