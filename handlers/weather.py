from aiogram import Router, types, F
from services.weather import get_weather

router = Router()

@router.message(F.text == "🌤 Ob-havo")
async def weather_handler(message: types.Message):
    await message.answer("🔄 Ob-havo ma'lumotlari yuklanmoqda...")
    weather_info = get_weather()
    await message.answer(weather_info, parse_mode="Markdown")