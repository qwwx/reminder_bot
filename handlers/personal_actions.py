from aiogram import types
from dispatcher import dp
from datetime import datetime
from bot import BotDB


@dp.message_handler(commands="start")
async def start(message: types.Message):
    if not BotDB.user_exists(message.from_user.id):
        BotDB.add_user(message.from_user.id)

    await message.bot.send_message(message.from_user.id, "Добро пожаловать!\nДля создания уведомления набери '/r "
                                                         "текст уведомления'")


@dp.message_handler(commands="r", commands_prefix="/!")
async def start(message: types.Message):
    value = message.text[3:]
    if len(value) == 0:
        await message.reply("✅ Попробуйте еще раз!")
    else:
        msg_text = value.find(':') + 3
        date = datetime.strptime(value[:msg_text], "%Y-%m-%d %H:%M")
        msg = value[msg_text + 1:]
        BotDB.add_record(message.from_user.id, msg, date)
        await message.reply("✅ Запись успешно внесена!")
