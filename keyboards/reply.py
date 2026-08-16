from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🌱 Ekin va O'g'it kalkulyatori"), KeyboardButton(text="📊 Bozor narxlari")],
        [KeyboardButton(text="👨‍🌾 Agro maslahatlar va Zararkunandalar")]
    ],
    resize_keyboard=True
)

crop_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🥕 Kechki sabzi"), KeyboardButton(text="🍂 Tamaki")],
        [KeyboardButton(text="🥔 Kartoshka"), KeyboardButton(text="❌ Bekor qilish")]
    ],
    resize_keyboard=True
)

fert_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Karbamid (Urea)"), KeyboardButton(text="Ammiakli selitra")],
        [KeyboardButton(text="❌ Bekor qilish")]
    ],
    resize_keyboard=True
)

cancel_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="❌ Bekor qilish")]],
    resize_keyboard=True
)