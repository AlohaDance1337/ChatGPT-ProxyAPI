import asyncio
import sys

from core.handlers import routers
from aiogram import Bot, Dispatcher
from core.tools.get_token import get_token
from core.tools.logger import Logger

log = Logger()
dp = Dispatcher()

async def main() -> None:
    try:
        bot = Bot(token=get_token('TG_token', 'Bot_TG'))
        dp.include_routers(*routers)
        await dp.start_polling(bot)
    except Exception as e:
        log.error(e)
        await bot.close()

if __name__ == "__main__":
    asyncio.run(main())