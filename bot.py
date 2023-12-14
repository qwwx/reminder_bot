import asyncio

import aioschedule
from aiogram import executor

from db import BotDB
from dispatcher import dp, bot

BotDB = BotDB('accountant.db')


async def send_message_to_users():
    info = BotDB.get_record()
    if len(info) != 0:
        id, text = BotDB.get_record()[0][0], BotDB.get_record()[0][1]
        tg_id = BotDB.tg_id(id)[0][0]
        await bot.send_message(tg_id, text)


async def scheduler():
    # здесь "ставим задачи на выполнение" каждую минуту
    aioschedule.every().minute.do(send_message_to_users)
    while True:
        # в бесконечном цикле дожидаемся, пока придёт задача
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):   # создаём асинхронную задачу
    asyncio.create_task(scheduler())


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
