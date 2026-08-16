from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

advice_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🐛 Sabzi pashshasi va Qurti", callback_data="pest_carrot")],
        [InlineKeyboardButton(text="🍂 Tamaki gullash va Qoltiq novdalar", callback_data="pest_tobacco")],
        [InlineKeyboardButton(text="🪲 Kolorado qo'ng'izi (Kartoshka)", callback_data="pest_potato")]
    ]
)