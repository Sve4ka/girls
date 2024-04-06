#  здесь описываются реакции кнопок на нажатие

from aiogram import types

import gpt.ml
import prog.creat_prod_fms
import prog.keyboard_creat as kb
import prog.static_text as txt
from prog.command import dp


@dp.callback_query_handler(text="start")
async def main_callback(call: types.CallbackQuery):
    await call.message.edit_text(text=txt.START_2, reply_markup=kb.start_kb())


@dp.callback_query_handler(text="buyer")
async def main_callback(call: types.CallbackQuery):
    await call.message.edit_text(text=txt.BUYER, reply_markup=kb.buyer_kb())


@dp.callback_query_handler(text="seller")
async def main_callback(call: types.CallbackQuery):
    await call.message.edit_text(text=txt.SELLER, reply_markup=kb.seller_kb())


@dp.callback_query_handler(text="profile_buyer")
async def main_callback(call: types.CallbackQuery):
    await call.message.edit_text(text=txt.PR_BUYER, reply_markup=kb.profile_buyer_kb())


@dp.callback_query_handler(text="profile_seller")
async def main_callback(call: types.CallbackQuery):
    await call.message.edit_text(text=txt.PR_SELLER, reply_markup=kb.profile_seller_kb())


@dp.callback_query_handler(text="profile")
async def main_callback(call: types.CallbackQuery):
    await call.message.edit_text(text=txt.PR, reply_markup=kb.profile_kb())


@dp.callback_query_handler(text="buy_product")
async def main_callback(call: types.CallbackQuery):
    await call.message.edit_text(text=txt.ERROR, reply_markup=kb.buy_product())


@dp.callback_query_handler(text="eat_product")
async def main_callback(call: types.CallbackQuery):
    await call.message.edit_text(text=txt.ERROR, reply_markup=kb.eat_product())


@dp.callback_query_handler(text="create_product")
async def main_callback(call: types.CallbackQuery):
    await call.message.edit_text(text=txt.CR_PR, reply_markup=kb.create_product_kb())


@dp.callback_query_handler(text="create_shop")
async def main_callback(call: types.CallbackQuery):
    await call.message.edit_text(text=txt.CR_SH, reply_markup=kb.create_shop_kb())


@dp.callback_query_handler(text="my_product")
async def main_callback(call: types.CallbackQuery):
    await call.message.edit_text(text=txt.MY_PR, reply_markup=kb.my_product_kb(call.from_user.id))


@dp.callback_query_handler(text="my_shop")
async def main_callback(call: types.CallbackQuery):
    await call.message.edit_text(text=txt.MY_SH, reply_markup=kb.my_shop_kb(call.from_user.id))


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('shop_'))
async def main_callback(call: types.CallbackQuery):
    await call.message.edit_text(text=txt.SH + "\n" + call.data, reply_markup=kb.shop_kb())


@dp.callback_query_handler(text="cancel_product")
async def main_callback(call: types.CallbackQuery):
    await call.message.edit_text(text=txt.MY_PR, reply_markup=kb.seller_kb())


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('product_'))
@dp.callback_query_handler(text="product")
async def main_callback(call: types.CallbackQuery):
    await call.message.edit_text(text=txt.DB_PR + "\n" + call.data + gpt.ml.gpt(call.data.split('_')[-1]), reply_markup=kb.product_kb(call.from_user.id))

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith("pred_page_"))
@dp.callback_query_handler(text="pred_page")
async def main_callback(call: types.CallbackQuery):
    await call.message.edit_text(text=txt.MY_PR + "\n" + call.data, reply_markup=kb.my_product_kb(call.from_user.id, int(call.data[-1]) - 1))

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith("next_page_"))
@dp.callback_query_handler(text="next_page")
async def main_callback(call: types.CallbackQuery):
    print(call.data)
    await call.message.edit_text(text=txt.MY_PR + "\n" + call.data, reply_markup=kb.my_product_kb(call.from_user.id, int(call.data[-1]) + 1))
