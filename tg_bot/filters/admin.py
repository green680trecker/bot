import typing
from tg_bot.models.connect_db import Filter
from aiogram.dispatcher.filters import BoundFilter


class AdminFilter(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin: typing.Optional[bool] = None):
        self.is_admin = is_admin

    async def check(self, obj):
        if self.is_admin is None:
            return False
        elif Filter().filter_admin(obj.from_user.id):
            return self.is_admin
