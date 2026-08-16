from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from config import ADMIN_ID
from database import get_all_prices, update_price_in_db
from keyboards.reply import cancel_keyboard, main_keyboard

router = Router()

class AdminPriceUpdate(StatesGroup):
    waiting_for_product = State()
    waiting_for_new_price = State()

@router.message(F.text == "📊 Bozor narxlari")
async def show_prices(message: types.Message):
    prices = get_all_prices()
    text = "📍 **Mang'it va Amudaryo dehqon bozorida joriy narxlar:**\n\n"
    for prod, prc in prices:
        text += f"🔹 **{prod}:** {prc}\n"
    await message.answer(text, parse_mode="Markdown")

@router.message(Command("admin"))
async def admin_start(message: types.Message, state: FSMContext):
    if message.from_user.id != ADMIN_ID:
        await message.answer("⚠️ Siz admin emassiz!")
        return
    await state.set_state(AdminPriceUpdate.waiting_for_product)
    await message.answer("Qaysi mahsulot narxini o'zgartirmoqchisiz?\n(Masalan: `Kartoshka`, `Piyoz` yoki `Sabzi`)", reply_markup=cancel_keyboard, parse_mode="Markdown")

@router.message(AdminPriceUpdate.waiting_for_product)
async def process_admin_prod(message: types.Message, state: FSMContext):
    await state.update_data(product=message.text)
    await state.set_state(AdminPriceUpdate.waiting_for_new_price)
    await message.answer(f"**{message.text}** uchun yangi narxni kiriting:", parse_mode="Markdown")

@router.message(AdminPriceUpdate.waiting_for_new_price)
async def process_admin_price(message: types.Message, state: FSMContext):
    data = await state.get_data()
    update_price_in_db(data['product'], message.text)
    await message.answer(f"✅ **{data['product']}** narxi muvaffaqiyatli yangilandi!", reply_markup=main_keyboard, parse_mode="Markdown")
    await state.clear()