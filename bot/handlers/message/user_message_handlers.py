from aiogram.filters import Command
from aiogram import Router, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from datetime import datetime

from ...keyboards import keyboards
from database.services.user_services import get_users, get_user_by_id, create_user

user_router = Router()



@user_router.message(Command('get_all_users'))
async def all_users(message: types.Message):
    try:
        existing_user = await get_user_by_id(int(message.chat.id))
        if existing_user:
            users = await get_users()
            print(users)
            for user in users:

                
                await message.answer(f"{user.photo_id}\n Name= {user.name}\nRegistration date= {user.date}")
                await message.answer_photo(user.photo_id,f"\n Name= {user.name}\nRegistration date= {user.date}")

            
        else:
            await message.answer("First you have to be registered 🙏😅", reply_markup=keyboards.register_reply_keyboard)
        # await message.answer(f"{users}")
    except Exception as e:
        await message.answer(f"Some error occurred: {e}")

@user_router.message(Command('all_users'))
async def all_users(message: types.Message):
    try:
        users = await get_users()
        await message.answer(f"{users}")
    except Exception as e:
        await message.answer(f"Some error occurred: {e}")

@user_router.message(Command('add_user'))
async def add_users(message: types.Message):
    try:
        print("Adding user...")
        users = await create_user(int(message.chat.id), name = message.chat.full_name, date= datetime.now())
        print("done")
        await message.answer(f"{users}")
    except Exception as e:
        await message.answer(f"Some error occurred:\n {e}")

@user_router.message(Command('get_user_by_id'))
async def get_by_id(message: types.Message):
    try:
        await message.answer("What is the id of the user you are looking for?")
    except:
        await message.answer("Some error occurred")

# @user_router.message()
# async def retrive_user_by_id(message: types.Message):
#     try:
#         print("searching user...")
#         user = await get_user_by_id(int(message.text))
#         print("searching complete...")
#         await message.answer(f"{user}")
#     except Exception as e:
#         await message.answer(f"Some error occurred {e}")


# Same way you can update and delete users