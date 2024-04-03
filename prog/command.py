#  здесь описывается реакция на различные команды + генерируется сам бот

from random import randint

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove


from prog.keyboard_creat import start_kb
from prog.static_text import HELP, HOME, START, STATISTIC, START_2

from config import TOKEN_API
import prog.static_text

bot = Bot(TOKEN_API)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer(START, parse_mode='HTML')
    await message.answer(text=START_2, reply_markup=start_kb())
    await message.delete()


@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await message.answer(HELP, parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['home'])
async def command_home(message: types.Message):
    await message.answer(HOME, parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['statistic'])
async def command_statistic(message: types.Message):
    await message.answer(STATISTIC, parse_mode='HTML')
    await message.delete()
