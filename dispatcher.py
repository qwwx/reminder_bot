import logging
import os
from aiogram import Bot, Dispatcher
from filters import IsOwnerFilter, IsAdminFilter, MemberCanRestrictFilter

# Configure logging
logging.basicConfig(level=logging.INFO)

# prerequisites
if not os.environ["BOT_TOKEN"]:
    exit("No token provided")

# init
bot = Bot(token=os.environ["BOT_TOKEN"], parse_mode="HTML")
dp = Dispatcher(bot)

# activate filters
dp.filters_factory.bind(IsOwnerFilter)
dp.filters_factory.bind(IsAdminFilter)
dp.filters_factory.bind(MemberCanRestrictFilter)
