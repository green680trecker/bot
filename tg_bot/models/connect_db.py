import pymysql.cursors

from tg_bot.config import load_config


class Base:
    """Connect to database and execute query"""
    __slots__ = {"config", "connection"}
    def __init__(self):
        self.config = load_config(".env")
        self.connection = pymysql.connect(
            host=self.config.db.host,
            port=3306,
            user=self.config.db.user,
            password=self.config.db.password,
            database=self.config.db.database,
            autocommit=True,
            # cursorclass=pymysql.cursors.DictCursor
        )

    def insert_id(self, id):
        """function for requester new users"""
        try:
            with self.connection.cursor() as cursor:
                qurery_sql = "SELECT * FROM users WHERE user_id == %s"
                cursor.execute(qurery_sql, id)
                us = cursor.fetchone()
                if not us:
                    u_sql = "INSERT INTO users(user_id) VALUES(%s)"
                    cursor.execute(qurery_sql, id)

        finally:
            self.connection.close()

    def insert_words(self, word_1, word_2):
        """function for insert new words"""
        try:
            with self.connection.cursor() as cursor:
                qurery_sql = "INSERT INTO word(word_en, word_ru) VALUES(%s, %s)"

                cursor.execute(qurery_sql, (word_1, word_2))

        except():
            print("Lol1")
        finally:
            self.connection.close()

    def select_words(self, limit=None, all=False):
        """function for select words"""
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT word_en, word_ru FROM word")
                if all is True:
                    rows = cursor.fetchall()
                else:
                    rows = cursor.fetchmany(limit)
        except Exception as ex:
            print(ex)

        finally:
            self.connection.close()
            return rows
    def select_word_id(self, id):
        """function for select word to id"""
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT word_en, word_ru FROM word WHERE id = %s", id)
                rows = cursor.fetchone()
        except Exception as ex:
            print(ex)

        finally:
            self.connection.close()
            return rows

# def test_base():
#
#
#     for i in y:
#         print(i[0], i[1])
#
# test_base()

def main(nums=2) -> None:
    if nums == 1:
        x = Base()
        y = x.select_words(all=True)
        print(y)
    elif nums == 2:
        x = Base()
        y = x.select_word_id(10)
        print(y)
    elif nums == 3:
        x = Base()
        y = x.select_word_id(10)
        my_list = str(y).split()
        print(y[1])



if __name__ == "__main__":
    # num = int(input("[INFO] Enter command from 1 till 3 :D\n"))
    main(3)

