#  имеено этот файл будет запускаться, здесь в основном запуск + призыв всех файлов которые требуются к работе

from random import choice
from time import time
from aiogram import executor, types
from aiogram.types import ReplyKeyboardRemove

from prog.command import dp
import prog.command, prog.static_text, prog.keyboard_creat, prog.keyboard_work, prog.fms_button
import gpt.ml, db.db


async def on_startup(_):
    print("HI, i work")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)