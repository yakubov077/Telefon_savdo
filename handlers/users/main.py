from aiogram.types import Message, CallbackQuery
from loader import dp, bot, ADMINS,CHANNELS
from aiogram import F
from aiogram.fsm.context import FSMContext
from states.reklama import Reklama
from aiogram.types import ReplyKeyboardRemove
from keyboard_buttons.inline.menu import ask, menu,holat_menu,menu_xotira,by
from keyboard_buttons.default.keyboard import tel, add

@dp.message(F.text=="Reklama qo'shish ➕")
async def reklama(message:Message,state:FSMContext):
    await message.answer("Reklama telefon uchun rasm 🖼 kiriting !",reply_markup=ReplyKeyboardRemove())
    await message.delete()
    await state.set_state(Reklama.rasm)

@dp.message(F.photo, Reklama.rasm)
async def reklama_rasm(message: Message, state: FSMContext):
    if message.photo:
        photo = message.photo[-1].file_id
        await state.update_data(photo=photo)
        await message.answer("Telefonni nomini kiriting ! 📱")
        await state.set_state(Reklama.nomi)

@dp.message(Reklama.rasm)
async def reklama_rasm_del(message:Message, state:FSMContext):
    await message.delete()
    await message.answer(text= "Iltimos telefon rasmini kiriting ❗️")

@dp.message(F.text, Reklama.nomi)
async def reklama_nomi(message:Message,state:FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer("Telefon xotira hajmini kiriting !",reply_markup=menu_xotira)
    await state.set_state(Reklama.dakument)

@dp.message(Reklama.nomi)
async def reklama_rasm_del(message:Message, state:FSMContext):
    await message.delete()
    await message.answer(text= "Iltimos telefon nomini  kiriting ❗️")

@dp.callback_query(F.data == "16_gb")
async def reklama_urtacha(callbeck:CallbackQuery,state:FSMContext):
    await callbeck.message.delete()
    await state.update_data(xotira="16 Gb")
    await callbeck.message.answer("Karopka dakument bormi yoki yo'qmi 📦📄", reply_markup=ask)
    await state.set_state(Reklama.dakument)

@dp.callback_query(F.data == "32_gb")
async def reklama_urtacha(callbeck:CallbackQuery,state:FSMContext):
    await callbeck.message.delete()
    await state.update_data(xotira="32 Gb")
    await callbeck.message.answer("Karopka dakument bormi yoki yo'qmi 📦📄", reply_markup=ask)
    await state.set_state(Reklama.dakument)

@dp.callback_query(F.data == "64_gb")
async def reklama_urtacha(callbeck:CallbackQuery,state:FSMContext):
    await callbeck.message.delete()
    await state.update_data(xotira="64 Gb")
    await callbeck.message.answer("Karopka dakument bormi yoki yo'qmi 📦📄", reply_markup=ask)
    await state.set_state(Reklama.dakument)

@dp.callback_query(F.data == "128_gb")
async def reklama_urtacha(callbeck:CallbackQuery,state:FSMContext):
    await callbeck.message.delete()
    await state.update_data(xotira="128 Gb")
    await callbeck.message.answer("Karopka dakument bormi yoki yo'qmi 📦📄", reply_markup=ask)
    await state.set_state(Reklama.dakument)

@dp.callback_query(F.data == "256_gb")
async def reklama_urtacha(callbeck:CallbackQuery,state:FSMContext):
    await callbeck.message.delete()
    await state.update_data(xotira="256 Gb")
    await callbeck.message.answer("Karopka dakument bormi yoki yo'qmi 📦📄", reply_markup=ask)
    await state.set_state(Reklama.dakument)

@dp.callback_query(F.data == "512_gb")
async def reklama_urtacha(callbeck:CallbackQuery,state:FSMContext):
    await callbeck.message.delete()
    await state.update_data(xotira="512 Gb")
    await callbeck.message.answer("Karopka dakument bormi yoki yo'qmi 📦📄", reply_markup=ask)
    await state.set_state(Reklama.dakument)

@dp.callback_query(F.data == "1_tb")
async def reklama_urtacha(callbeck:CallbackQuery,state:FSMContext):
    await callbeck.message.delete()
    await state.update_data(xotira="1 TB")
    await callbeck.message.answer("Karopka dakument bormi yoki yo'qmi 📦📄", reply_markup=ask)
    await state.set_state(Reklama.dakument)

@dp.callback_query(F.data == "2_tb")
async def reklama_urtacha(callbeck:CallbackQuery,state:FSMContext):
    await callbeck.message.delete()
    await state.update_data(xotira="2 TB")
    await callbeck.message.answer("Karopka dakument bormi yoki yo'qmi 📦📄", reply_markup=ask)

@dp.callback_query(F.data == "yes")
async def reklama_yes(callbeck:CallbackQuery,state:FSMContext):
    await callbeck.message.delete()
    await state.update_data(dakument="Bor")
    await callbeck.message.answer("Telefonnig holati ! ⚙️",reply_markup=holat_menu)
    await state.set_state(Reklama.holati)

@dp.callback_query(F.data == "no")
async def reklama_no(callbeck:Message,state:FSMContext):
    await callbeck.message.delete()
    await state.update_data(dakument="Yo'q")
    await callbeck.message.answer("Telefonnig holati ! ⚙️",reply_markup=holat_menu)
    await state.set_state(Reklama.holati)

@dp.message(Reklama.dakument)
async def reklama_dakument_del(message:Message, state:FSMContext):
    await message.delete()
    await message.answer(text= "Iltimos tugmalardan birini tanlang ❗️")

@dp.callback_query(F.data == "ideal")
async def reklama_ideal(callbeck:CallbackQuery,state:FSMContext):
    await callbeck.message.delete()
    await state.update_data(holati="Ideal")
    await callbeck.message.answer("Telefonnig narxini kiriting ! 💵")
    await state.set_state(Reklama.narx)
    
@dp.callback_query(F.data == "o'rtacha")
async def reklama_urtacha(callbeck:CallbackQuery,state:FSMContext):
    await callbeck.message.delete()
    await state.update_data(holati="O'rtacha")
    await callbeck.message.answer("Telefonnig narxini kiriting ! 💵")
    await state.set_state(Reklama.narx)


@dp.callback_query(F.data == "yaxshi")
async def reklama_yaxshi(callbeck:CallbackQuery,state:FSMContext):
    await callbeck.message.delete()
    await state.update_data(holati="Yaxshi")
    await callbeck.message.answer("Telefonnig narxini kiriting ! 💵")
    await state.set_state(Reklama.narx)

@dp.callback_query(F.data == "yomon")
async def reklama_yomon(callbeck:Message,state:FSMContext):
    await callbeck.message.delete()
    await state.update_data(holati="Yomon")
    await callbeck.message.answer("Telefonning narxini kiriting ! 💵",)
    await state.set_state(Reklama.narx)

@dp.message(Reklama.holati)
async def reklama_dakument_del(message:Message, state:FSMContext):
    await message.delete()
    await message.answer(text= "Iltimos telfon holatini tugmalardan tanlang ❗️")


@dp.message(F.text, Reklama.narx)
async def reklama_narx(message:Message,state:FSMContext):
    narx = message.text
    await state.update_data(narx=narx)
    await message.answer("Telefon raqamingizni kiriting ! 📞",reply_markup=tel)
    await state.set_state(Reklama.tel)


@dp.message(Reklama.narx)
async def reklama_rasm_del(message:Message, state:FSMContext):
    await message.delete()
    await message.answer(text= "Iltimos telefon narxini kiriting ❗️")

@dp.message(F.contact, Reklama.tel)
async def reklama_narx(message:Message,state:FSMContext):
    if message.contact:  # Foydalanuvchi tugma orqali raqamni yuborgan bo'lsa
        tel = message.contact.phone_number
    else:  # Foydalanuvchi qo'lda raqam yozgan bo'lsa
        tel = message.text
    await state.update_data(tel=tel)
    await message.answer("Qushimcha malumot kiriting ! 📎\nMisol uchun :\n\n1 - Bonus 🎁\n2 - Telfon kamerasi 📷\n3 - Tezkor xotirasi 💾\n4 - telfon xaqida qushimcha ma'lumot 📝",reply_markup=ReplyKeyboardRemove())
    await state.set_state(Reklama.qushmch_m)


@dp.message(Reklama.tel)
async def reklama_rasm_del(message:Message, state:FSMContext):
    await message.delete()
    await message.answer(text= "Iltimos telfon raqamni tug'ri kiriting ❗️")


@dp.message(F.text, Reklama.qushmch_m)
async def reklama_tel(message: Message, state: FSMContext):
    qushmcha_m = message.text
    await state.update_data(qushmcha_m=qushmcha_m)
    await message.answer("ABMEN ♻️ (telfoni almashtirish)", reply_markup=by)
    await state.set_state(Reklama.abmen)

@dp.message(Reklama.qushmch_m)
async def reklama_rasm_del(message:Message, state:FSMContext):
    await message.delete()
    await message.answer(text= "Iltimos telefon ma'lumotini kiriting ❗️")

@dp.callback_query(F.data == "yes1")
async def reklama_yes(callbeck:CallbackQuery,state:FSMContext):
    await callbeck.message.delete()
    await state.update_data(abmen="Bor")
    await callbeck.message.answer("Manzilingizni kiriting ! 📍",reply_markup=ReplyKeyboardRemove())
    await state.set_state(Reklama.shahar)

@dp.callback_query(F.data == "no1")
async def reklama_no(callbeck:Message,state:FSMContext):
    await callbeck.message.delete()
    await state.update_data(abmen="Yo'q")
    await callbeck.message.answer("Manzilingizni kiriting ! 📍",reply_markup=ReplyKeyboardRemove())
    await state.set_state(Reklama.shahar)

@dp.message(Reklama.abmen)
async def reklama_dakument_del(message:Message, state:FSMContext):
    await message.delete()
    await message.answer(text= "Iltimos tugmalardan birini tanlang ❗️")

@dp.message(F.text,Reklama.shahar)
async def reklama(message:Message,state:FSMContext):
    data = await state.get_data()
    photo = data.get("photo")
    name = data.get("name")
    xotira = data.get("xotira")
    dakument = data.get("dakument")
    holat = data.get("holati")
    narx = data.get("narx")
    tel = data.get("tel")
    abmen = data.get("abmen")
    qushmcha_m = data.get("qushmcha_m")
    shahar = message.text
    user = message.from_user.username
    text = f"📱 Telefon nomi : {name}\n💾 Xotirasi : {xotira}\n📦📄 Karobka dakument : {dakument}\n⚙️ Holati : {holat}\n♻️ Abmen : {abmen}\n💵 Narxi : {narx}\n📝 Qushimcha ma'lumot : {qushmcha_m}\n\n📞 Telefon raqami : {tel}\nTelegram lichkasi 📩 @{user}\nManzil 📍 : {shahar}\n\n ❗️ Telefonni ko'rmasdan to'lov qilmang Admin savdoga javobgar emas."

    await bot.send_photo(chat_id=ADMINS[0], photo=photo, caption=text, reply_markup=menu)

    await message.answer("Reklama adminga yuborildi qabulqilsa javob keladi ! 📨",reply_markup=add)
    await state.clear()

@dp.message(Reklama.shahar)
async def reklama_rasm_del(message:Message, state:FSMContext):
    await message.delete()
    await message.answer(text= "Iltimos manzilingizni tug'ri kiriting ❗️")

@dp.callback_query(F.data == "True")
async def reklama_true(callbeck:Message,state:FSMContext):
    await callbeck.message.delete()
    user = callbeck.message.caption.split()[-1]
    photo = callbeck.message.photo[-1].file_id
    text = callbeck.message.caption
    await bot.send_photo(chat_id=CHANNELS[0], photo=photo, caption=text)
    await bot.send_photo(chat_id=user, photo=photo, caption=text)    
    await bot.send_message(chat_id=user, text="Tabriklimiz reklama adminga ma'qul keldi\n\nQayta reklama yuborish uchun pastdagi tugmani bosing 👇🏻")

@dp.callback_query(F.data == "False")
async def reklama_false(callbeck:Message,state:FSMContext):
    await callbeck.message.delete()
    photo = callbeck.message.photo[-1].file_id

    user = callbeck.message.caption.split()[-1] # Foydalanuvchi id
    text = callbeck.message.caption[:-12] # xabar id yo'q

    await bot.send_photo(chat_id=user, photo=photo, caption=text)
    await bot.send_message(chat_id=user, text="Afsuski reklama adminga maqul kelmadi \n\nQayta reklama yuborish uchun pastdagi tugmani bosing 👇🏻")