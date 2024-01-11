from aiogram.filters import Command
from aiogram import Router, types 
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from utils.state import UserForm,QuizForm,QuestionForm
# from ..keyboards import keyboard
from ...keyboards import keyboards
from database.services.user_services import get_users, get_user_by_id, create_user,is_admin,get_contributor_questions,is_blocked


message_router = Router()

@message_router.message(Command('start'))
async def start_handler(message: types.Message):
    try:
        existing_user = await get_user_by_id(int(message.chat.id))
        if existing_user:
            await message.answer("Check the following services",reply_markup=keyboards.services_reply_keyboard)
            blocked=await is_blocked(int(message.chat.id))
            if blocked:
                await message.answer("🚫 Apologies, but it seems that your access to the bot has been temporarily restricted. If you believe this is an error or have questions regarding the restriction, please reach out to our support team at [sbsena@gmail.com]. We appreciate your understanding and cooperation. Thank you. 🤖 #BotAccess")
            else:
                await message.answer(f"🚀 Welcome aboard, quiz enthusiast! 🌟 Get ready to embark on a journey of knowledge and fun. Sharpen your wits, challenge your friends, and let the quest for wisdom begin! 🧠✨. May the best mind prevail! 🏆 #QuizTime")


                    # admin=await is_admin(int(message.chat.id))
                    # # if admin:
                    # #     await message.answer("Hello Admin")
                
        else:
            await message.answer(f"🚀 Welcome aboard, quiz enthusiast! 🌟 Get ready to embark on a journey of knowledge and fun. Sharpen your wits, challenge your friends, and let the quest for wisdom begin! 🧠✨. May the best mind prevail! 🏆 #QuizTime")
            await message.answer("Let's start by registering you", reply_markup=keyboards.register_reply_keyboard)

    except  Exception as e:
        print(e)

        await message.answer("Some error occurred")
        await message.answer(f"{e}")

@message_router.message()
async def check_message(message: types.Message,state: FSMContext) -> None:
    try:
        

            if message.text == "👋 Register!":
                
                try:
                    existing_user = await get_user_by_id(int(message.chat.id))
                    if existing_user:
                        blocked=await is_blocked(int(message.chat.id))
                        if blocked:
                            await message.answer("🚫 Apologies, but it seems that your access to the bot has been temporarily restricted. If you believe this is an error or have questions regarding the restriction, please reach out to our support team at [sbsena@gmail.com]. We appreciate your understanding and cooperation. Thank you. 🤖 #BotAccess")
                        else:
                        
                            await message.answer("You Have Already registered, you can just use the following services",reply_markup=keyboards.after_register_inline_keyboard)
                    else:
                        

                        await message.answer("Here you will be providing your required inUserFormation in order to be registered 🙂")
                        await state.set_state(UserForm.name)
                        await message.answer("Enter Your Name : ")
                except   Exception as e:
                    await message.answer(f"Some error occurred {e}")


            elif message.text == "📃 Start Quiz":

                existing_user = await get_user_by_id(int(message.chat.id))
                if existing_user:
                    blocked=await is_blocked(int(message.chat.id))
                    if blocked:
                        await message.answer("🚫 Apologies, but it seems that your access to the bot has been temporarily restricted. If you believe this is an error or have questions regarding the restriction, please reach out to our support team at [sbsena@gmail.com]. We appreciate your understanding and cooperation. Thank you. 🤖 #BotAccess")
                    else:
                        state.clear()
                        await state.set_state(QuizForm.category)
                        await message.answer("Let's Start Your fist by choosing Quiz questions Category ",reply_markup=keyboards.categories_inline_keyboard)



                        
                else:
                    await message.answer("Let's start by registering you", reply_markup=keyboards.register_reply_keyboard)
                    


                
            elif message.text == "👏 Contribute new Question":
                existing_user = await get_user_by_id(int(message.chat.id))
                if existing_user:
                    
                    blocked=await is_blocked(int(message.chat.id))
                    if blocked:
                        await message.answer("🚫 Apologies, but it seems that your access to the bot has been temporarily restricted. If you believe this is an error or have questions regarding the restriction, please reach out to our support team at [sbsena@gmail.com]. We appreciate your understanding and cooperation. Thank you. 🤖 #BotAccess")
                    else:
                        state.clear()


                        await state.set_state(QuestionForm.category)
                        await message.answer("Select Category : ")

                        
                else:
                    await message.answer("Let's start by registering you", reply_markup=keyboards.register_reply_keyboard)
                await message.answer(f"Let's create a question for a quiz")



            elif message.text=="💪 My Contribution":
                
                existing_user = await get_user_by_id(int(message.chat.id))
                if existing_user:
                    await message.answer("Check the following services",reply_markup=keyboards.services_reply_keyboard)
                    blocked=await is_blocked(int(message.chat.id))
                    if blocked:
                        await message.answer("🚫 Apologies, but it seems that your access to the bot has been temporarily restricted. If you believe this is an error or have questions regarding the restriction, please reach out to our support team at sbsena@gmail.com. We appreciate your understanding and cooperation. Thank you. 🤖 #BotAccess")
                    else:


                        questions=await get_contributor_questions(int(message.from_user.id))
                        if questions:
                            for question in questions:
                                await message.answer(f"*Question*= {question.title}\n*Choices*\nA.  {question.choices[0]}\tB.  {question.choices[1]}\nC.  {question.choices[2]}\tD.  {question.choices[3]}\nAnswer= '{question.answer}'\n*Category*= {question.category}\t *Level*= {question.level}\n *Status*= #{question.status}")
                        else:
                            await message.answer("You haven't contribute by any question yet😢",reply_markup=keyboards.services_reply_keyboard)
                        

                        
                else:
                    await message.answer("Let's start by registering you", reply_markup=keyboards.register_reply_keyboard)
 
                
                
            else:
                await message.answer("Unknown command")
    except Exception as e:
        print(e)
        await message.answer(f"{e}")  