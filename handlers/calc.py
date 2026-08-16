from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.reply import crop_keyboard, fert_keyboard, cancel_keyboard, main_keyboard

router = Router()

class CropCalc(StatesGroup):
    waiting_for_crop = State()
    waiting_for_area = State()
    waiting_for_fertilizer = State()

@router.message(F.text == "🌱 Ekin va O'g'it kalkulyatori")
async def start_crop_calc(message: types.Message, state: FSMContext):
    await state.set_state(CropCalc.waiting_for_crop)
    await message.answer("Qaysi ekin uchun o'g'it hisoblamoqchisiz?", reply_markup=crop_keyboard)

@router.message(CropCalc.waiting_for_crop, F.text.in_(["🥕 Kechki sabzi", "🍂 Tamaki", "🥔 Kartoshka"]))
async def process_crop(message: types.Message, state: FSMContext):
    await state.update_data(selected_crop=message.text)
    await state.set_state(CropCalc.waiting_for_area)
    await message.answer(f"Tanlandi: **{message.text}**\nMaydon hajmini **sotix**da kiriting:", reply_markup=cancel_keyboard, parse_mode="Markdown")

@router.message(CropCalc.waiting_for_area)
async def process_area(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Iltimos, faqat raqam kiriting:")
        return
    await state.update_data(user_area=int(message.text))
    await state.set_state(CropCalc.waiting_for_fertilizer)
    await message.answer("O'g'it turini tanlang:", reply_markup=fert_keyboard)

@router.message(CropCalc.waiting_for_fertilizer, F.text.in_(["Karbamid (Urea)", "Ammiakli selitra"]))
async def process_result(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    crop, area, fert = user_data['selected_crop'], user_data['user_area'], message.text
    norm = 1.0 if fert == "Karbamid (Urea)" else 1.2
    total = area * norm
    await message.answer(
        f"✅ **Natija:** {area} sotix {crop} uchun **{total:.1f} kg** {fert} tavsiya etiladi.",
        reply_markup=main_keyboard,
        parse_mode="Markdown"
    )
    await state.clear()