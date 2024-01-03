
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from typing import List


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



# inline keyboard with callback
after_register_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Start Quiz", callback_data="start_quiz"),
            InlineKeyboardButton(text="Create new Quiz Question", callback_data="create_quiz")
        ]
    ]
)


# inline keyboard with callback
choice_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="A.", callback_data="a"),
            InlineKeyboardButton(text="B.", callback_data="b"),
            InlineKeyboardButton(text="C.", callback_data="c"),
            InlineKeyboardButton(text="D.", callback_data="d"),
        ]
    ]
)


def choice_inline_keyboard(choices: List[str]) -> InlineKeyboardMarkup:
    # print(choices)
    inlines=[]
    try:
        for choice in choices:
            inlines.append(InlineKeyboardButton(text=choice, callback_data=f"answer_{choice}"))
        keyboard = InlineKeyboardMarkup(inline_keyboard=[inlines[0:2],inlines[2:]])
        return keyboard
    except Exception as e:
        print(e)
