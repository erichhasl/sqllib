import sqlite3


class SQLConnection:

    def __init__(self, path):
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()

    def query(self, command):
        self.cursor.execute(command)
        return self.cursor.fetchall()

    def commit(self):
        self.connection.commit()
