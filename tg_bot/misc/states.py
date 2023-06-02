from aiogram.dispatcher.filters.state import StatesGroup, State


class Brain_test(StatesGroup):
    q1 = State()
    q2 = State()

class Add_word(StatesGroup):
    firstandlast = State()


class Show_word(StatesGroup):
    st_show = State()

class English_test(StatesGroup):
    eg1 = State()
    eg2 = State()


