from aiogram import types, Dispatcher
from aiogram.utils.markdown import hcode
from bot.pwdgen import XKCD

async def cmd_generate_weak(message: types.Message):
    # вызов пресета weak
    pwd: XKCD = message.bot.get("pwd")
    await message.answer(hcode(pwd.weak()))

async def cmd_generate_normal(message: types.Message):
    # вызов пресета normal
    pwd: XKCD = message.bot.get("pwd")
    await message.answer(hcode(pwd.normal()))

async def cmd_generate_strong(message: types.Message):
    # вызов пресета strong
    pwd: XKCD = message.bot.get("pwd")
    await message.answer(hcode(pwd.strong()))

# вот здесь можно добавить свою функцию для вызова пресета

# регистрация команд
def register_commands(dp: Dispatcher):
    # обработчик вызывает пресет weak по команде generate_weak
    dp.register_message_handler(cmd_generate_weak, commands="generate_weak")

    # обработчик вызывает пресет normal по команде generate_normal
    dp.register_message_handler(cmd_generate_normal, commands="generate_normal")

    # обработчик вызывает пресет strong по команде generate_strong
    dp.register_message_handler(cmd_generate_strong, commands="generate_strong")

    # вот здесь можно добавить свою команду
