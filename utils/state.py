from aiogram.fsm.state import StatesGroup, State

class UserForm(StatesGroup):
    name = State()
    phone_number = State()
    photo_id = State()



class QuestionForm(StatesGroup):
    title = State()
    category=State()
    level=State()
    option_a= State()
    option_b = State()
    option_c = State()
    option_d = State()
    answer = State()


class QuizForm(StatesGroup):
    WaitingForAnswer = State()
    QuizComplete = State()



class QuizQuestionsForm(StatesGroup):
    question_1=State()
    question_2=State()
    question_3=State()
    question_4=State()
    question_5=State()
    correct_answer=State()

