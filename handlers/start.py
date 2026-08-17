from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from database import add_user
from keyboards.reply import main_keyboard

router = Router()

@router.message(CommandStart())
async def start_handler(message: types.Message, state: FSMContext):
    await state.clear()
    
    # Foydalanuvchini bazaga saqlash
    add_user(
        user_id=message.from_user.id,
        full_name=message.from_user.full_name,
        username=message.from_user.username or "Mavjud emas"
    )
    
    await message.answer(
        f"Salom, {message.from_user.first_name}!\nAgro-yordamchi botga xush kelibsiz.",
        reply_markup=main_keyboard
    )

@router.message(F.text == "❌ Bekor qilish")
async def cancel_handler(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Jarayon bekor qilindi.", reply_markup=main_keyboard)