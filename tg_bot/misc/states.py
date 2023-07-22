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


class Forward_for_admin_message(StatesGroup):
    f_d = State()


class Forward_for_admin_photo(StatesGroup):
    f_d_p1 = State()
    f_d_p2 = State()


class St_photo(StatesGroup):
    ph = State()


class Add_state(StatesGroup):
    st = State()


class Del_admin_state(StatesGroup):
    st = State()


class Del_user_state(StatesGroup):
    st = State()


class Doc_state(StatesGroup):
    st = State()


class Base_ii(StatesGroup):
    st = State()

class Image_ii(StatesGroup):
    st = State()

class Mp3_state(StatesGroup):
    st = State()