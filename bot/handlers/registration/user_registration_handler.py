from aiogram.filters import Command
from aiogram import Router, types, F 
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ContentType
from aiogram.filters import Command
from datetime import datetime
from ...keyboards import keyboards
from utils.state import UserForm
from database.services.user_services import  create_user

user_registration_router = Router()


@user_registration_router.message(Command('Register'))
async def name_UserForm(message: Message, state: FSMContext):
    print(message.text)
    
    try:
        await message.answer("Here you will be providing your required inUserFormation in order to be registered 🙂")
        await state.set_state(UserForm.name)
        await message.answer("Enter Your Name : ")
    except:
        await message.answer("Some error occurred")


@user_registration_router.message(UserForm.name)
async def phone_UserForm(message: Message, state:FSMContext):
    try:
        await state.update_data(name=message.text)
        await state.set_state(UserForm.photo_id)
        await message.answer("Let's Continue with your profile pic")
    except:
        await message.answer("Some error occurred")


@user_registration_router.message(UserForm.photo_id)
async def phone_UserForm(message: Message, state:FSMContext):
    try:
        
        await state.update_data(photo_id = message.photo[-1].file_id)
        await state.set_state(UserForm.phone_number)
        await message.answer("Enter your phone number")
    except:
        await message.answer("Some error occurred")

@user_registration_router.message(UserForm.phone_number)
async def UserForm_photo(message: Message, state:FSMContext):
    try:
        await state.update_data(phone_number = message.text)
        

        data=await state.get_data()


        print("Adding user...")
        users = await create_user(int(message.chat.id), name=data['name'],phone_number=data['phone_number'],photo_id=data['photo_id'] ,date=datetime.now(),is_admin=0)
        print("done")
        await message.answer("You have been successfully register👏")
        await message.answer("Now you are allowed to check the following services",reply_markup=keyboards.after_register_inline_keyboard)
        await message.answer("/get_all_users   -> View the list of Registered User")


    except Exception as e:

        await message.answer(f"Some error occurred {e}")

