from aiogram.filters import Command
from aiogram import Router, types 
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram.types import ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from database.services.question_services import get_questions,create_question
from database.services.user_services import is_admin

from bot.keyboards import keyboards
from utils.state import QuestionForm,QuizForm
question_registration_router = Router()



@question_registration_router.callback_query(lambda c: c.data=="create_quiz",)
async def process_callback_respond_to_create_quiz(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer(f"Let's create a question for a quiz")
    try:
        await state.set_state(QuestionForm.category)
        await callback_query.message.answer("Select Category : ")

        # await state.set_state(QuestionForm.title)
        # await callback_query.message.answer("Enter the Question : ")
    except Exception as e:
        print(e)
        await callback_query.message.answer(f"{e}")


# insert level
@question_registration_router.message(QuestionForm.category)
async def process_callback_respond_to_create_quiz(message: types.Message, state: FSMContext):
    try:
        await state.update_data(category=message.text)
        await state.set_state(QuestionForm.level)
        await message.answer("Enter Level : ")
    except Exception as e:
        print(e)
        await message.answer(f"{e}")
        
# insert question
@question_registration_router.message(QuestionForm.level)
async def process_callback_respond_to_create_quiz(message: types.Message, state: FSMContext):
    try:
        await state.update_data(level=message.text)
        await state.set_state(QuestionForm.title)
        await message.answer("Enter the Question : ")
    except Exception as e:
        print(e)
        await message.answer(f"{e}")
    
@question_registration_router.message(QuestionForm.title)
async def process_callback_respond_to_create_quiz(message: types.Message, state: FSMContext):
    try:
        await state.update_data(title=message.text)
        await state.set_state(QuestionForm.option_a)
        await message.answer("Enter Option A : ")
    except Exception as e:
        print(e)
        await message.answer(f"{e}")
@question_registration_router.message(QuestionForm.option_a)
async def process_callback_respond_to_create_quiz(message: types.Message, state: FSMContext):
    try:
        await state.update_data(option_a=message.text)
        await state.set_state(QuestionForm.option_b)
        await message.answer("Enter Option B : ")
    except Exception as e:
        print(e)
        await message.answer(f"{e}")

@question_registration_router.message(QuestionForm.option_b)
async def process_callback_respond_to_create_quiz(message: types.Message, state: FSMContext):
    try:
        await state.update_data(option_b=message.text)
        await state.set_state(QuestionForm.option_c)
        await message.answer("Enter Option C : ")
    except Exception as e:
        print(e)
        await message.answer(f"{e}")

@question_registration_router.message(QuestionForm.option_c)
async def process_callback_respond_to_create_quiz(message: types.Message, state: FSMContext):
    try:
        await state.update_data(option_c=message.text)
        await state.set_state(QuestionForm.option_d)
        await message.answer("Enter Option D : ")
    except Exception as e:
        print(e)
        await message.answer(f"{e}")


@question_registration_router.message(QuestionForm.option_d)
async def process_callback_respond_to_create_quiz(message: types.Message, state: FSMContext):
    try:
        await state.update_data(option_d=message.text)
        await state.set_state(QuestionForm.answer)
        await message.answer("Enter Answer : ")
    except Exception as e:
        print(e)
        await message.answer(f"{e}")



# create the overall data
@question_registration_router.message(QuestionForm.answer)
async def process_callback_respond_to_create_quiz(message: types.Message, state: FSMContext):
    try:
        data=await state.get_data()
        options = [data['option_a'], data['option_b'], data['option_c'], data['option_d']]
        provided_answer = message.text.strip()

        if provided_answer not in options:
            raise ValueError(f"❌The provided answer '{provided_answer}' is not among the available options. Please select a valid answer from the provided options.🙏")

        await state.update_data(answer=message.text)
        data=await state.get_data()
        print(data)
        print("Adding question...")
        admin=await is_admin(int(message.chat.id))
        question = await create_question(title=data['title'],category=data['category'],level=data['level'], choices=[data['option_a'],data['option_b'],data['option_c'],data['option_d']],answer=data['answer'], status=  "approved" if (admin) else "requested" ,user_id=  message.chat.id)
        print("done")
        if(not admin):
            await message.answer("🙌 Thank you for your contribution! 🌟 You've just added a question to our quiz bank. Your dedication to enriching the quiz experience is truly appreciated. 🧠✨ Our team will review and approve your question shortly. Once accepted, it'll become part of the challenge for fellow quizzers! Stay tuned and keep the questions coming! 🚀 #QuizContributor")
        else:
            await message.answer("You have successfully created a question👏")
        await state.clear()
    except ValueError as ve:
        await message.answer(f" {ve}")
    except Exception as e:

        await message.answer(f"Some error occurred {e}")



def showQuestion(question,callback_query: types.CallbackQuery):
    try:
        print("inside showQuestion")
        inline_keyboard = keyboards.choice_inline_keyboard(question.choices)
        callback_query.message.answer(f"{question.title}", reply_markup=inline_keyboard)
    except Exception as e:
        print(e)
        callback_query.message.answer(f"{e}")
