import sqlitelib


if __name__ == '__main__':

    db = sqlitelib.SQLiteDatabase("test.db")
    table = db.get_table("data")
    # table.insert({"fname": "'Lise Lotte'"})
    print(table)
    print(table.select("number, fname", "fname='Lise Lotte' AND"
          " (number=5 OR number=5)"))
