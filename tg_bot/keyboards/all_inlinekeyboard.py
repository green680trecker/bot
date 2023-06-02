from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Inner_board:
    def __init__(self, text, link=None, callback=None):
        self.text = text
        self.link = link
        self.callback = callback

    @staticmethod
    def keyboard_coffee():

        mark = InlineKeyboardMarkup(row_width=2)
        return mark.add(InlineKeyboardButton(text="touch me", callback_data="touch"),
                        #"https://www.youtube.com/channel/UCcm00p5w8nPQ2INFv8waXJg"
                        InlineKeyboardButton(text="My Youtube", callback_data="link"))
    @staticmethod
    def keyboard_show_word():
        mark = InlineKeyboardMarkup(row_width=2)
        return mark.add(InlineKeyboardButton(text="Yes", callback_data="Yes"),
                        InlineKeyboardButton(text="Show all", callback_data="show_all"))


    # def inner_keyboard_data(text, url=None, callback=None):
    #     return InlineKeyboardButton(text=text, url=url, callback_data=callback)
    #
    # @staticmethod
    # def inline_markup(b):
    #     ik = InlineKeyboardMarkup(row_width=2)
    #     return ik.add(b)


