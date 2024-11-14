from aiogram.types import Message, CallbackQuery
from loader import dp, bot, ADMINS,CHANNELS
from aiogram import F
from aiogram.fsm.context import FSMContext
from states.reklama import Reklama
from aiogram.types import ReplyKeyboardRemove
from keyboard_buttons.inline.menu import ask, menu

@dp.message(F.text=="Reklama qo'shish ➕")
async def reklama(message:Message,state:FSMContext):
    await message.answer("Reklama telefon uchun 🖼 rasm kiriting !", reply_markup=ReplyKeyboardRemove())
    await state.set_state(Reklama.rasm)
    
@dp.message(Reklama.rasm)
async def reklama_rasm(message:Message, state:FSMContext):
    photo = message.photo[-1].file_id
    await state.update_data(photo = photo)
    await message.answer("Telefonni nomini kiriting !")
    await state.set_state(Reklama.nomi)

@dp.message(Reklama.nomi)
async def reklama_nomi(message:Message,state:FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer("Telefon xotira hajmini kiriting !")
    await state.set_state(Reklama.xotira)

@dp.message(Reklama.xotira)
async def reklama_xotira(message:Message,state:FSMContext):
    xotira = message.text
    await state.update_data(xotira=xotira)
    await message.answer("Karopka dakument bormi yoki yo'qmi", reply_markup=ask)
    await state.set_state(Reklama.dakument)

@dp.callback_query(F.data == "yes")
async def reklama_yes(callbeck:CallbackQuery,state:FSMContext):
    await callbeck.message.delete()
    await state.update_data(dakument="Bor")
    await callbeck.message.answer("Telefonnig holati haqida yozing !")
    await state.set_state(Reklama.holati)

@dp.callback_query(F.data == "no")
async def reklama_no(callbeck:Message,state:FSMContext):
    await callbeck.message.delete()
    await state.update_data(dakument="Yo'q")
    await callbeck.message.answer("Telefonnig holati haqida yozing !")
    await state.set_state(Reklama.holati)

# @dp.message(Reklama.dakument)
# async def reklama(message:Message,state:FSMContext):
#     await state.update_data(=)
#     await message.answer("")
#     await state.set_state(Reklama.holati)

@dp.message(Reklama.holati)
async def reklama(message:Message,state:FSMContext):
    data = await state.get_data()
    photo = data.get("photo")
    name = data.get("name")
    xotira = data.get("xotira")
    dakument = data.get("dakument")
    holat = message.text
    user = message.from_user.id
    
    text = f"📱{name}\n💾{xotira}\n📦{dakument}\n⚙️{holat}\n  {user}"

    await bot.send_photo(chat_id=ADMINS[0], photo=photo, caption=text, reply_markup=menu)

    await message.answer("Reklama adminga yuborildi qabulqilsa javob keladi !")
    await state.clear()
    
@dp.callback_query(F.data == "True")
async def reklama_true(callbeck:Message,state:FSMContext):
    await callbeck.message.delete()
    photo = callbeck.message.photo[-1].file_id
    text = callbeck.message.caption
    await bot.send_photo(chat_id=CHANNELS[0], photo=photo, caption=text)

@dp.callback_query(F.data == "False")
async def reklama_false(callbeck:Message,state:FSMContext):
    await callbeck.message.delete()
    photo = callbeck.message.photo[-1].file_id

    user = callbeck.message.caption.split()[-1] # Foydalanuvchi id
    text = callbeck.message.caption[:-12] # xabar id yo'q

    await bot.send_photo(chat_id=user, photo=photo, caption=text)
    await bot.send_message(chat_id=user, text="Reklama maqul kelmadi boshqatadan to'diring !")
    


# @dp.message(Reklama.yili)
# async def reklama(message:Message,state:FSMContext):
#     await state.update_data(=)
#     await message.answer("")
#     await state.set_state(Reklama.rang)

# @dp.message(Reklama.rang)
# async def reklama(message:Message,state:FSMContext):
#     await state.update_data(=)
#     await message.answer("")
#     await state.set_state(Reklama.tel)

# @dp.message(Reklama.tel)
# async def reklama(message:Message,state:FSMContext):
#     await state.update_data(=)
#     await message.answer("")
#     await state.set_state(Reklama.tg_user)

# @dp.message(Reklama.tg_user)
# async def reklama(message:Message,state:FSMContext):
#     await state.update_data(=)
#     await message.answer("")
#     await state.set_state(Reklama.shahar)

# @dp.message(Reklama.shahar)
# async def reklama(message:Message,state:FSMContext):
#     await state.update_data(=)
#     await message.answer("")






















# agar erklama qoniqarli bo'lmasa foydalanuvchiga admin xabar yuborsin