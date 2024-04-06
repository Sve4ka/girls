from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton

import db.db
import gpt.ml
import prog.static_text
from prog import keyboard_creat as kb
from prog.command import dp

NEW_PROD = """
СОЗДАЕМ НОВЫЙ ПРОДУКТ
Название   {}
Тип        {}
"""


class ProductStates(StatesGroup):
    name = State()
    wait = State()
    end = State()


async def update_keyboard(state: FSMContext):
    async with state.proxy() as data:
        nn = data['name']
        fv = data['fr_ve']
        call = data['callback']
        if nn != "None":
            tt = kb.create_product_kb()
            tt.add(InlineKeyboardButton(text='all okey', callback_data="cr_pr_ok"))
            await call.message.edit_text(text="проверьте введенные данные и если все "
                                              "верно нажмите на клавишу all okey \n\n" +
                                              NEW_PROD.format(nn, fv)+gpt.ml.gpt(nn).split('\n')[0],
                                         reply_markup=tt)
        else:
            await call.message.edit_text(NEW_PROD.format(nn, fv), reply_markup=kb.create_product_kb())


@dp.callback_query_handler(text='create_product', state="*")
async def new_fr(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(name="None")
    await state.update_data(fr_ve="Фрукт")
    await state.update_data(callback=call)
    await update_keyboard(state)


@dp.callback_query_handler(text='name_product', state="*")
async def inl_new_fr_name(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("введите имя", reply_markup=kb.create_product_kb())
    await ProductStates.name.set()


@dp.callback_query_handler(text='fr_ve_product', state="*")
async def inl_new_fr_name(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        fv = data['fr_ve']
        if fv == "Фрукт":
            await state.update_data(fr_ve="Овощ")
        else:
            await state.update_data(fr_ve="Фрукт")
        await update_keyboard(state)


@dp.callback_query_handler(text='cancel_product', state='*')
async def new_cancel(call: types.CallbackQuery, state: FSMContext):
    if state is None:
        return
    await state.finish()
    await call.message.edit_text("создание продукта принудительно завершено, продукт не был сохранен",
                                 reply_markup=kb.seller_kb())


@dp.callback_query_handler(text='cr_pr_ok', state="*")
async def inl_new_fr_name(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        nn = data['name']
        ss = (data['fr_ve'] == "Фрукт")
        db.db.add_product(nn, ss)
    await state.finish()
    await call.message.edit_text("Данные сохранены\n\n" + prog.static_text.SELLER.capitalize(), reply_markup=kb.seller_kb())


@dp.message_handler(state=ProductStates.name)
async def price_state(message: types.Message, state: FSMContext):
    name = message.text.lower()
    await state.update_data(name=name)
    await update_keyboard(state)
    await message.delete()
    await state.set_state(ProductStates.wait.state)


@dp.message_handler(state=ProductStates.wait)
async def wait_state(message: types.Message, state: FSMContext):
    await update_keyboard(state)
