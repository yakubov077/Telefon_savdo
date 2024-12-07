from aiogram.types import Message
from loader import dp,db
from aiogram.filters import CommandStart
from keyboard_buttons.default.keyboard import add

@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) 
        await message.answer(text=f"""Assalomu alaykum !   {full_name} \nSizni <b>Telefon Savdo 📱</b> botida ko'rishdan xursndmiz 🎉\n\nQuyidagi tugma yordamida bizni xizmatimizdan foydalaning :\n
<b>Reklama qo'shish</b> ➕  Bizning kanalga reklama junataish 🚀\n
Shartlar ❗\nYuborgan reklamangizni admin Tasdiqlasa ✅ Kanalga reklama boradi !""",parse_mode='html', reply_markup=add)
   
    except:
        await message.answer(text=f"""Assalomu alaykum !   {full_name} \nSizni <b>Telefon Savdo 📱</b> botida ko'rishdan xursndmiz ! 🎉\n\nQuyidagi tugma yordamida bizni xizmatimizdan foydalaning :\n
<b>Reklama qo'shish</b> ➕  Bizning kanalga reklama junataish 🚀\n
Shartlar ❗\nYuborgan reklamangizni admin Tasdiqlasa kanalga reklama boradi !""",parse_mode='html', reply_markup=add)
