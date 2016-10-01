import sqlitelib


if __name__ == '__main__':

    db = sqlitelib.SQLiteDatabase("test.db")
    table = db.get_table("data")
    # table.insert({"fname": "'Lise Lotte'"})
    print(table)
    print(table.select("number, fname", "fname='Lise Lotte' AND"
          " (number=5 OR number=6)"))

    print(table.select("fname", "fname='Lise Lotte' AND"
          " (number=5 OR number=6)", True))

    table2 = db.get_table("stuff")
    table2.insert({"name": "'Seil'", "owner": "'Lise Lotte'", "age": "7"})
    print(table2.select(conditions="age > 5"))
