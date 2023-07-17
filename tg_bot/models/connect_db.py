import pymysql.cursors

from tg_bot.config import load_config


class Base:
    """Connect to database and execute query"""
    __slots__ = {"config", "connection", "id"}

    def __init__(self, id: int = 0):
        self.id = id
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
    def insert_words(self, word_1, word_2):
        """function for insert new words"""
        try:
            with self.connection.cursor() as cursor:
                qurery_sql = "INSERT INTO word(word_en, word_ru) VALUES(%s, %s)"

                cursor.execute(qurery_sql, (word_1, word_2))

        except():
            print("Error in insert_words")
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

    def select_word_id(self):
        """function for select word to id"""
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT word_en, word_ru FROM word WHERE id = %s", self.id)
                rows = cursor.fetchone()
        except Exception as ex:
            print(ex)

        finally:
            self.connection.close()
            return rows


class AdminQuery(Base):
    def add_admin(self) -> None:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE `users` SET useradmin=True WHERE user_id = {user_id}".format(user_id=self.id))
        except:
            print("Error in add_admin")

        finally:
            self.connection.close()

    def delete_admin(self) -> None:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE `users` SET useradmin=False WHERE user_id = {user_id}".format(user_id=self.id))
        except:
            print("Error in delete_admin")
        finally:
            self.connection.close()
    def delete_user(self) -> None:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM users WHERE user_id = {user_id}".format(user_id=self.id))
        except:
            print("Error in delete_user")
        finally:
            self.connection.close()


class NewUser(Base):
    def add_user(self, username=None):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "SELECT EXISTS(SELECT user_id FROM users WHERE user_id = {user_id})".format(user_id=self.id))
                res = cursor.fetchone()
                if res[0] == False:
                    cursor.execute(
                        "INSERT INTO users(user_id, username) VALUES ({user_id}, '{username}')".format(user_id=self.id, username=username))
                    return True
                else:
                    return False
        except:
            print("Error in add_user")
        finally:
            self.connection.close()


class Filter(Base):
    def filter_admin(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "SELECT EXISTS(SELECT useradmin FROM users WHERE user_id = {user_id} and useradmin = True)".format(user_id=self.id))
                res = cursor.fetchone()
                if res[0] == True:
                    return True
                else:
                    return False
        except:
            print("Error in filter_admin")

        finally:
            self.connection.close()


