import re  # Import the regular expression module

from aiogram.filters import Command
from aiogram import Router, types, F 
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ContentType
from aiogram.filters import Command
from datetime import datetime
from ...keyboards import keyboards
from utils.state import UserForm
from database.services.user_services import  get_user_by_id, create_user

user_registration_router = Router()


@user_registration_router.message(Command('Register'))
async def name_UserForm(message: Message, state: FSMContext):
    print(message.text)
    
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


@user_registration_router.message(UserForm.name)
async def photo_UserForm(message: Message, state:FSMContext):
    print("I am after name registe")
    try:
        name = message.text.strip()  # Remove leading and trailing whitespaces
        if not name:
            raise ValueError("Name cannot be empty. Please enter a valid name.")

        await state.update_data(name=name)
        await state.set_state(UserForm.photo_id)
        await message.answer("Let's continue with your profile pic")

    except ValueError as ve:
        await message.answer(f"Invalid input: {ve}")

    except Exception as e:
        await message.answer(f"Some error occurred: {e}")


@user_registration_router.message(UserForm.photo_id)
async def phone_UserForm(message: Message, state:FSMContext):
    try:
        if not message.photo:
            raise ValueError("No photo provided. Please send a photo.")

        await state.update_data(photo_id=message.photo[-1].file_id)
        await state.set_state(UserForm.phone_number)
        await message.answer("Enter your phone number")

    except ValueError as ve:
        await message.answer(f"Invalid input: {ve}")

    except Exception as e:
        await message.answer(f"Some error occurred: {e}")
        
        
@user_registration_router.message(UserForm.phone_number)
async def UserForm_finish(message: Message, state:FSMContext):
    try:
        # Validate phone number using a regular expression
        phone_number = message.text
        if not re.match(r'^\d{10}$', phone_number):  # Assuming a valid phone number has 10 digits
            raise ValueError("Invalid phone number format. Please enter a 10-digit number.")

        await state.update_data(phone_number = message.text)
        

        data=await state.get_data()


        print("Adding user...")
        users = await create_user(int(message.chat.id), name=data['name'],phone_number=data['phone_number'],photo_id=data['photo_id'] ,date=datetime.now(),is_admin=0,status=1)
        print("done")
        await state.clear()
        await message.answer("You have been successfully register👏",reply_markup=keyboards.services_reply_keyboard)
        await message.answer("Check the following services",reply_markup=keyboards.services_reply_keyboard)
        


    except ValueError as ve:
        await message.answer(f"Invalid input: {ve}")

    except Exception as e:
        await message.answer(f"Some error occurred: {e}")

