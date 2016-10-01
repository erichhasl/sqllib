import database
import connection


class SQLiteDatabase(database.Database):

    def __init__(self, path):
        self.db = connection.SQLConnection(path)
