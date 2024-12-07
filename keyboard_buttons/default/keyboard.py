from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

tel = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Telefon raqam yuborish ☎️', request_contact=True)]
    ],
    resize_keyboard=True
)


add = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Reklama qo'shish ➕"),
        ]
        
    ],
   resize_keyboard=True,
   input_field_placeholder="Menudan birini tanlang"
)

