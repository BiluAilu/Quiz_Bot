
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from typing import List
from utils import constants


register_reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👋 Register!")
        ],
     
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Register",
    selective=True
)
services_reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📃 Start Quiz")],
        [
            KeyboardButton(text="👏 Contribute by Question")
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
categories_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            
            InlineKeyboardButton(text="Programming", callback_data="category_Programming") ,
            InlineKeyboardButton(text="Networking", callback_data="Networking"),
         
        ],
        [
            
            InlineKeyboardButton(text="Health", callback_data="category_Health") ,
            InlineKeyboardButton(text="Sport", callback_data="category_Sport"),
         
        ],
      
        [
            
            InlineKeyboardButton(text="Physics", callback_data="category_Physics") ,
            InlineKeyboardButton(text="Other", callback_data="category_Other"),
         
        ]
    ]
)
level_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            
            InlineKeyboardButton(text="Easy", callback_data="level_easy") ,
            InlineKeyboardButton(text="Medium", callback_data="level_medium"),
            InlineKeyboardButton(text="Hard", callback_data="level_hard"),
         
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
