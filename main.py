import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import config
from database import init_db
from handlers import start, calc, prices, advice, weather

async def main():
    init_db()
    logging.basicConfig(level=logging.INFO)
    
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()

    # Routerlarni ulash
    dp.include_router(start.router)
    dp.include_router(calc.router)
    dp.include_router(prices.router)
    dp.include_router(advice.router)
    dp.include_router(weather.router)

    print("Bot muvaffaqiyatli ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())