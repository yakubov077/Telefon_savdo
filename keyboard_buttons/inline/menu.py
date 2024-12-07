from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

f_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Adminga junatish ✈️", callback_data="tasdiqlash"), InlineKeyboardButton(text="Tahrirlash ✏️", callback_data="tahrirlash")]
    ]
)

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Tasdiqlash ✅", callback_data="True"), InlineKeyboardButton(text="Bekor qilish ❌", callback_data="False")]
    ]
)

ask = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Bor", callback_data="yes"), InlineKeyboardButton(text="Yo'q", callback_data="no")]
    ]
)

by = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Bor", callback_data="yes1"), InlineKeyboardButton(text="Yo'q", callback_data="no1")]
    ]
)

holat_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ideal 100%", callback_data="ideal"), InlineKeyboardButton(text="Yaxshi 75%", callback_data="yaxshi")],
        [InlineKeyboardButton(text="O'rtacha 50%", callback_data="o'rtacha"), InlineKeyboardButton(text="Yomon 25%", callback_data="yomon")]
    ]
)

menu_xotira = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="16 Gb", callback_data="16_gb"), InlineKeyboardButton(text="32 Gb", callback_data="32_gb")],
        [InlineKeyboardButton(text="64 Gb", callback_data="64_gb"), InlineKeyboardButton(text="128 Gb", callback_data="128_gb")],
        [InlineKeyboardButton(text="256 Gb", callback_data="256_gb"), InlineKeyboardButton(text="512 Gb", callback_data="512_gb")],
        [InlineKeyboardButton(text="1 TB", callback_data="1_tb"), InlineKeyboardButton(text="2 TB", callback_data="2_tb")],
    ]
)
