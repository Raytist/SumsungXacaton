import asyncio
from aiogram import Bot
from aiogram import Dispatcher
from configs import *
from handler import router
bot = Bot(TG_TOKEN)
dp = Dispatcher()
async def main():
    dp.include_router(router=router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


