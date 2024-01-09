from aiogram.filters import Command
from aiogram import Router, types, F 
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ContentType
from aiogram.filters import Command
from datetime import datetime
from ...keyboards import keyboards
from utils.state import QuizQuestionsForm,QuizForm
from database.services.user_services import  create_user
from database.services.question_services import get_questions,create_question
from utils import constants

quiz_taking_router = Router()


questions=[]
score=0
@quiz_taking_router.callback_query(lambda c: c.data == "start_quiz")
async def category_form(callback_query: types.CallbackQuery, state: FSMContext):
    
    try:
        await state.clear()
        await state.set_state(QuizForm.category)
        await callback_query.message.answer("Let's Start Your fist by choosing Quiz questions Category ",reply_markup=keyboards.categories_inline_keyboard)
    except Exception as e:
        print(e)
        callback_query.message.answer(f"{e}")
        
        
@quiz_taking_router.callback_query(lambda c: c.data.startswith("category"))
async def level_form(callback_query: types.CallbackQuery, state: FSMContext):

    try:
        await state.update_data(category=callback_query.data.replace("category_", ""))
        await state.set_state(QuizForm.level)
        await callback_query.message.answer("Now choose the difficulty level",reply_markup=keyboards.level_inline_keyboard)

    except Exception as e:
        print(e)
        callback_query.message.answer(f"{e}")
        
@quiz_taking_router.callback_query(lambda c: c.data.startswith("level"))
async def start_quiz(callback_query: types.CallbackQuery, state: FSMContext):
    global questions
    global score
    score=0


    try:
        await state.update_data(level=callback_query.data.replace("level_", ""))
        data = await state.get_data()
        category=data.get("category")
        level=data.get("level")

        questions = await get_questions(category, level)
        if len(questions)<5:

            await callback_query.message.answer("Sorry, There is no available amount of question for current category and level🙏😓")
        else:
            
            await callback_query.message.answer(f"""🌟 Welcome to the Quiz Adventure! 🚀 Get ready to test your knowledge in the {category} category at the {level} level. Here's how it works:\n\n🔍 Each question will appear one at a time.\n⏱️ You have a limited time to answer, so think fast!\n👉 Choose the correct option by tapping the corresponding answer.""")
            inline_keyboard = keyboards.choice_inline_keyboard(questions[0].choices)
            await callback_query.message.answer(f"Q1. {questions[0].title}", reply_markup=inline_keyboard)
            # await callback_query.message.answer("Enter your answer",reply_markup=keyboards.quiz_answer_inline_keyboard)
            await state.update_data(correct_answer=questions[0].answer)
            await state.set_state(QuizQuestionsForm.question_1)
        # await callback_query.message.answer("Enter Your Name : ")
    except Exception as e:
        print(e)
        callback_query.message.answer(f"{e}")


@quiz_taking_router.callback_query(lambda c: c.data.startswith("answer"))
async def process_callback_answer(callback_query: types.CallbackQuery, state: FSMContext):



    
    global score
    user_answer = callback_query.data.replace("answer_", "")


    data = await state.get_data()
    correct_answer = data.get("correct_answer")

    if user_answer == correct_answer:

        score += 1
        await callback_query.message.answer("✅Correct answer!")
    else:
        await callback_query.message.answer(f"❌Wrong answer! \nThe correct answer is *{correct_answer}*")
        
    if await state.get_state() == QuizQuestionsForm.question_1:
        await state.update_data(correct_answer=questions[1].answer)
        await state.set_state(QuizQuestionsForm.question_2)
        inline_keyboard = keyboards.choice_inline_keyboard(questions[1].choices)
        await callback_query.message.answer(f"Q2. {questions[1].title}", reply_markup=inline_keyboard)

    elif await state.get_state() == QuizQuestionsForm.question_2:
        await state.update_data(correct_answer=questions[2].answer)
        await state.set_state(QuizQuestionsForm.question_3)
        inline_keyboard = keyboards.choice_inline_keyboard(questions[2].choices)
        await callback_query.message.answer(f"Q3. {questions[2].title}", reply_markup=inline_keyboard)

    elif await state.get_state() == QuizQuestionsForm.question_3:
        await state.update_data(correct_answer=questions[3].answer)
        await state.set_state(QuizQuestionsForm.question_4)
        inline_keyboard = keyboards.choice_inline_keyboard(questions[3].choices)
        await callback_query.message.answer(f"Q4. {questions[3].title}", reply_markup=inline_keyboard)

    elif await state.get_state() == QuizQuestionsForm.question_4:
        await state.update_data(correct_answer=questions[4].answer)
        await state.set_state(QuizQuestionsForm.question_5)
        inline_keyboard = keyboards.choice_inline_keyboard(questions[4].choices)
        await callback_query.message.answer(f"Q5. {questions[4].title}", reply_markup=inline_keyboard)
    
    elif await state.get_state() == QuizQuestionsForm.question_5:
        await state.clear()
        await callback_query.message.answer(f"""🎉 Congratulations! You've completed the quiz! 🌟\n\nYour Score: {score} out of 5\n\n{constants.customized_messages(score)}\n\nThank you for participating and embracing the challenge. Feel free to play again, explore new topics, or challenge your friends to beat your score! Keep the quest for knowledge alive! 🧠✨ #QuizMaster""")





