from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#about commands
@dp.message(Command("about"))
async def about_commands(message:Message):
    await message.answer("Bu bot nima qila oladi ?\n\nBu botda siz guruhga reklama junata olasiz")

