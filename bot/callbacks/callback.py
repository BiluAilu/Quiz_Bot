from aiogram.filters import Command
from aiogram import Router, types 
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram.types import ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from database.services.question_services import get_questions,create_question
from database.services.user_services import is_admin

from bot.keyboards import keyboards
from utils.state import QuestionForm,QuizForm
callback_router = Router()



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
        question = await create_question(title=data['title'],category=data['category'],level=data['level'], choices=[data['option_a'],data['option_b'],data['option_c'],data['option_d']],answer=data['answer'], status=  "approved" if (admin) else "requested" ,user_id=  message.chat.id)
        print("done")
        await message.answer("You have been successfully created a question👏")
        if(not admin):
            await message.answer("🙌 Thank you for your contribution! 🌟 You've just added a question to our quiz bank. Your dedication to enriching the quiz experience is truly appreciated. 🧠✨ Our team will review and approve your question shortly. Once accepted, it'll become part of the challenge for fellow quizzers! Stay tuned and keep the questions coming! 🚀 #QuizContributor")


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


# @callback_router.callback_query(lambda c: c.data == "start_quiz")
# async def process_callback_respond_to_start_quiz(callback_query: types.CallbackQuery, state: FSMContext, score=0):
#     await callback_query.message.answer("Let's Start Your quiz")

#     try:
#         questions = await get_questions("Programming", "easy")
#         # print(questions)

#         totalQuestion=len(questions)
#         score=0
#         for i in range(totalQuestion):
#             showQuestion(questions[i],callback_query)
#             # Send the question and choices with inline buttons
#             # inline_keyboard = keyboards.choice_inline_keyboard(question.choices)
#             # await callback_query.message.answer(f"{question.title}", reply_markup=inline_keyboard)

#             # Store the correct answer in the state for later comparison
#             await state.update_data(correct_answer=questions[i].answer)


#         # Update the user's state to track the current question
#         # await state.set_state(QuizForm.WaitingForAnswer)

#         # for question in questions:
#         #     print(question)
#         #     # Send the question and choices with inline buttons
#         #     inline_keyboard = keyboards.choice_inline_keyboard(question.choices)
#         #     await callback_query.message.answer(f"{question.title}", reply_markup=inline_keyboard)

#         #     # Store the correct answer in the state for later comparison
#         #     await state.update_data(correct_answer=question.answer)

#         # Move to the state to track the end of the quiz
#         print("I am in finish state")
#         await state.set_state(QuizForm.QuizComplete)

#     except Exception as e:
#         print(e)
#         await callback_query.message.answer(f"{e}")

# @callback_router.callback_query(lambda c: c.data.startswith("answer"))
# async def process_callback_answer(callback_query: types.CallbackQuery, state: FSMContext, score=0):
#     # Extract user's answer from the callback data
#     user_answer = callback_query.data.replace("answer_", "")

#     # Compare the user's answer with the correct answer stored in the state
#     data = await state.get_data()
#     correct_answer = data.get("correct_answer")

#     if user_answer == correct_answer:
#         # Handle correct answer, update user's score or perform other actions
#         score += 1
#         await callback_query.message.answer("Correct answer!")
#         return 1
#     else:
#         # Handle incorrect answer
#         await callback_query.message.answer("Incorrect answer!")
#         return 0

#     # # Check if the quiz is complete
#     # print(await state.get_state())
#     # print(await state.get_state() == QuizForm.QuizComplete)
#     # if await state.get_state() == QuizForm.QuizComplete:
#     #     # Finish the quiz
#     #     await callback_query.message.answer(f"Quiz complete! Your score: {score}")
#     #     await state.clear()
#     # else:
#     #     # Move to the next question
#     #     await state.set_state(QuizForm.WaitingForAnswer)
