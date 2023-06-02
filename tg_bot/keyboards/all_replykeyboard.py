from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

class Reply_board:

    @staticmethod
    def replay_keyboard(*args):
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)
        if len(args) == 1:
            return kb.add(KeyboardButton(text=args[0]))
        elif len(args) == 2:
            return kb.add(KeyboardButton(text=args[0]), KeyboardButton(text=args[1]))
        elif len(args) == 3:
            return kb.add(KeyboardButton(text=args[0]), KeyboardButton(text=args[1]), KeyboardButton(text=args[2]))
        elif len(args) == 4:
            return kb.add(KeyboardButton(text=args[0]), KeyboardButton(text=args[1]),
                          KeyboardButton(text=args[2]), KeyboardButton(text=args[3]))