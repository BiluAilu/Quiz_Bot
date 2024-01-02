
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton


register_reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/Register")
        ],
     
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Register",
    selective=True
)
