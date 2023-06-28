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


class Word(Base):
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


class AdminQuery(Base):
    def add_admin(self, user_id: int) -> None:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE `users` SET useradmin=True WHERE user_id = {user_id}".format(user_id=user_id))
        except:
            print("Error in add_admin")

        finally:
            self.connection.close()

    def delete_admin(self, user_id: int) -> None:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE `users` SET useradmin=False WHERE user_id = {user_id}".format(user_id=user_id))
        except:
            print("Error in delete_admin")
        finally:
            self.connection.close()
    def delete_user(self, user_id: int) -> None:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM users WHERE user_id = {user_id}".format(user_id=user_id))
        except:
            print("Error in delete_user")
        finally:
            self.connection.close()


class NewUser(Base):
    def add_user(self, user_id: int, username=None):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "SELECT EXISTS(SELECT user_id FROM users WHERE user_id = {user_id})".format(user_id=user_id))
                res = cursor.fetchone()
                if res[0] == False:
                    cursor.execute(
                        "INSERT INTO users(user_id, username) VALUES ({user_id}, '{username}')".format(user_id=user_id, username=username))
                    return True
                else:
                    return False
        # except:
        #     print("Error in add_user")
        finally:
            self.connection.close()
# NewUser().add_user(1646574179)

class Filter(Base):
    def filter_admin(self, user_id: int):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "SELECT EXISTS(SELECT useradmin FROM users WHERE user_id = {user_id} and useradmin = True)".format(user_id=user_id))
                res = cursor.fetchone()
                if res[0] == True:
                    return True
                else:
                    return False
        except:
            print("Error in filter_admin")

        finally:
            self.connection.close()


