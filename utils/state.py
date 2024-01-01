from aiogram.fsm.state import StatesGroup, State

class UserForm(StatesGroup):
    name = State()
    phone_number = State()
    role = State()
    photo = State()



class QuestionForm(StatesGroup):
    title = State()
    choice1= State()
    choice2 = State()
    choice3 = State()
    choice4 = State()
    answer = State()


