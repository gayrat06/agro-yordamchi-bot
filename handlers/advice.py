from aiogram import Router, types, F
from keyboards.inline import advice_inline_keyboard

router = Router()

@router.message(F.text == "👨‍🌾 Agro maslahatlar va Zararkunandalar")
async def show_advice_menu(message: types.Message):
    await message.answer("Kerakli ekin yoki zararkunanda turini tanlang:", reply_markup=advice_inline_keyboard)

@router.callback_query(F.data == "pest_carrot")
async def carrot_advice(call: types.CallbackQuery):
    await call.message.answer(
        "🥕 **Kechki sabzini pashsha va qurtlardan himoya qilish:**\n\n"
        "1. **Bargdan oziqlantirish:** Yosh nihollar 3-4 cm bo'lganda o'g'it solingach, iloji boricha tezda va mo'l sug'orilishi kerak.\n"
        "2. **Zararkunandalar:** Sabzi pashshasiga qarshi 'Karate' yoki 'Decis' preparatlarini me'yorida purkash tavsiya etiladi.",
        parse_mode="Markdown"
    )
    await call.answer()

@router.callback_query(F.data == "pest_tobacco")
async def tobacco_advice(call: types.CallbackQuery):
    await call.message.answer(
        "🍂 **Tamaki parvarishi (Gullash va Qoltiq novdalar):**\n\n"
        "1. **Chilim/Qoltiq novdalar:** Bosh poyadagi gullar va yon qoltiq novdalar (suckers) o'z vaqtida 2-3 marta qayirib olib tashlanishi shart.\n"
        "2. Bu amal barglarning qalinlashishi va hosil sifatining keskin oshishiga olib keladi.",
        parse_mode="Markdown"
    )
    await call.answer()

@router.callback_query(F.data == "pest_potato")
async def potato_advice(call: types.CallbackQuery):
    await call.message.answer(
        "🪲 **Kolorado qo'ng'iziga qarshi kurash:**\n\n"
        "1. **Kimyoviy ishlov:** Qo'ng'iz va lichinkalar paydo bo'lganda 'Coragen' yoki 'Prestige' vositalaridan foydalaning.",
        parse_mode="Markdown"
    )
    await call.answer()