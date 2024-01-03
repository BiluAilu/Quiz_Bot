from aiogram.filters import Command
from aiogram import Router, types 
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram.types import ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from database.services.question_services import get_questions,create_question
from database.services.user_services import is_admin

from bot.keyboards import keyboards
from utils.state import QuestionForm
callback_router = Router()




@callback_router.callback_query(lambda c: c.data=="start_quiz")
async def process_callback_respond_to_start_quiz(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f"Let's Start Your quiz")
    try:
        questions=await get_questions("Programming","easy")
        print(type(questions))
        for question in list(questions):
            await callback_query.message.answer(f"{question.title}",reply_markup=keyboards.choice_inline_keyboard)
    except Exception as e:
        print(e)
        await callback_query.message.answer(f"{e}")




@callback_router.callback_query(lambda c: c.data=="create_quiz",)
async def process_callback_respond_to_create_quiz(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer(f"Let's create a question for a quiz")
    try:

        await state.set_state(QuestionForm.title)
        await callback_query.message.answer("Enter Question Title : ")
    except Exception as e:
        print(e)
        await callback_query.message.answer(f"{e}")

@callback_router.message(QuestionForm.title)
async def process_callback_respond_to_create_quiz(message: types.Message, state: FSMContext):
    try:
        await state.update_data(title=message.text)
        await state.set_state(QuestionForm.option_a)
        await message.answer("Enter Option A : ")
    except Exception as e:
        print(e)
        await message.answer(f"{e}")
@callback_router.message(QuestionForm.option_a)
async def process_callback_respond_to_create_quiz(message: types.Message, state: FSMContext):
    try:
        await state.update_data(option_a=message.text)
        await state.set_state(QuestionForm.option_b)
        await message.answer("Enter Option B : ")
    except Exception as e:
        print(e)
        await message.answer(f"{e}")

@callback_router.message(QuestionForm.option_b)
async def process_callback_respond_to_create_quiz(message: types.Message, state: FSMContext):
    try:
        await state.update_data(option_b=message.text)
        await state.set_state(QuestionForm.option_c)
        await message.answer("Enter Option C : ")
    except Exception as e:
        print(e)
        await message.answer(f"{e}")

@callback_router.message(QuestionForm.option_c)
async def process_callback_respond_to_create_quiz(message: types.Message, state: FSMContext):
    try:
        await state.update_data(option_c=message.text)
        await state.set_state(QuestionForm.option_d)
        await message.answer("Enter Option D : ")
    except Exception as e:
        print(e)
        await message.answer(f"{e}")


@callback_router.message(QuestionForm.option_d)
async def process_callback_respond_to_create_quiz(message: types.Message, state: FSMContext):
    try:
        await state.update_data(option_d=message.text)
        await state.set_state(QuestionForm.answer)
        await message.answer("Enter Answer : ")
    except Exception as e:
        print(e)
        await message.answer(f"{e}")

# insert category
@callback_router.message(QuestionForm.answer)
async def process_callback_respond_to_create_quiz(message: types.Message, state: FSMContext):
    try:
        await state.update_data(answer=message.text)
        await state.set_state(QuestionForm.category)
        await message.answer("Enter Category : ")
    except Exception as e:
        print(e)
        await message.answer(f"{e}")

# insert level
@callback_router.message(QuestionForm.category)
async def process_callback_respond_to_create_quiz(message: types.Message, state: FSMContext):
    try:
        await state.update_data(category=message.text)
        await state.set_state(QuestionForm.level)
        await message.answer("Enter Level : ")
    except Exception as e:
        print(e)
        await message.answer(f"{e}")

# create the overall data
@callback_router.message(QuestionForm.level)
async def process_callback_respond_to_create_quiz(message: types.Message, state: FSMContext):
    try:
        await state.update_data(level=message.text)
        data=await state.get_data()
        print(data)
        print("Adding question...")
        admin=await is_admin(int(message.chat.id))
        question = await create_question(title=data['title'],category=data['category'],level=data['level'], choices=[data['option_a'],data['option_b'],data['option_c'],data['option_d']],answer=data['answer'], status=  "approved" if (admin) else "requested" ,user_id=  str(message.chat.id))
        print("done")
        await message.answer("You have been successfully created a question👏")
        if(not admin):
            await message.answer("This question will be reviewed by the admins and then can be used to end user, \Thank You for Your support!!!")


    except Exception as e:

        await message.answer(f"Some error occurred {e}")



