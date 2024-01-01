from aiogram.filters import Command
from aiogram import Router, types 
from aiogram.utils.keyboard import InlineKeyboardBuilder

# from ..keyboards import keyboard

message_router = Router()

@message_router.message(Command('start'))
async def start_handler(message: types.Message):
    try:
        await message.answer("Hello Welcome to Telegram Bot Development Phase")
    except  Exception as e:
        print(e)

        await message.answer("Some error occurred")
        await message.answer(f"{e}")

