from aiogram.filters import Command
from aiogram import Router, types 
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from utils.state import UserForm,QuizForm
# from ..keyboards import keyboard
from ...keyboards import keyboards
from database.services.user_services import get_users, get_user_by_id, create_user,is_admin
from database.services.user_services import get_users, get_user_by_id, create_user

message_router = Router()

@message_router.message(Command('start'))
async def start_handler(message: types.Message):
    try:
        # await message.answer(f"Hello {message.from_user.username}, Welcome to Quiz bot")
        await message.answer(f"🚀 Welcome aboard, quiz enthusiast! 🌟 Get ready to embark on a journey of knowledge and fun. Sharpen your wits, challenge your friends, and let the quest for wisdom begin! 🧠✨ Type /help to explore the wonders that await you. May the best mind prevail! 🏆 #QuizTime")

        existing_user = await get_user_by_id(int(message.chat.id))
        if existing_user:
            await message.answer("Now you are allowed to check the following services",reply_markup=keyboards.after_register_inline_keyboard)

            admin=await is_admin(int(message.chat.id))
            # if admin:
            #     await message.answer("Hello Admin")
            
        else:
            await message.answer("Let's start by registering you", reply_markup=keyboards.register_reply_keyboard)

    except  Exception as e:
        print(e)

        await message.answer("Some error occurred")
        await message.answer(f"{e}")

@message_router.message()
async def check_message(message: types.Message,state: FSMContext) -> None:
    if message.text == "👋 Register!":
        try:
            existing_user = await get_user_by_id(int(message.chat.id))
            if existing_user:
                await message.answer("You Have Already registered, you can just use the following services",reply_markup=keyboards.after_register_inline_keyboard)
            else:
                

                await message.answer("Here you will be providing your required inUserFormation in order to be registered 🙂")
                await state.set_state(UserForm.name)
                await message.answer("Enter Your Name : ")
        except   Exception as e:
            await message.answer(f"Some error occurred {e}")

    
    elif message.text == "📃 Start Quiz":
        try:
            await state.set_state(QuizForm.category)
            await message.answer("Let's Start Your fist by choosing Quiz questions Category ",reply_markup=keyboards.categories_inline_keyboard)
        except Exception as e:
            print(e)
            await message.answer(f"{e}") 
        
    elif message.text == "👏 Contribute by Question":
        await message.answer(f"Let's create a question for a quiz")
        try:
            await state.set_state(QuestionForm.category)
            await callback_query.message.answer("Select Category : ")
        except Exception as e:
            print(e)
            await callback_query.message.answer(f"{e}")


    else:
        await message.answer("Unknown command")
