import connection


class Database:

    def __init__(self):
        raise(NotImplementedError, "Should not be used! Use a subclass!")
        self.db = connection.SQLConnection("error")

    def get_table(self, name):
        tables = self.db.query("""SELECT name FROM sqlite_master
                                   WHERE type='table'
                                   AND name='{0}'""".format(name))
        if len(tables) == 0:
            raise(KeyError, "Could not find table")
            return
        return Table(tables[0][0], self.db)


class Table:

    def __init__(self, name, db):
        self.name = name
        self.db = db

    def __repr__(self):
        return str(self.db.query("""SELECT * FROM {0}""".format(self.name)))

    def insert(self, entries):
        """
        Insert the given entries into the table

        Arguments:
        entries -- dictionary
        """
        keys, vals = list(entries.keys()), list(entries.values())
        cmd_raw = "INSERT INTO {name} ({keys}) VALUES ({values});"
        cmd = cmd_raw.format(name=self.name,
                             keys=",".join(keys),
                             values=",".join(vals))
        print("Command", cmd)
        self.db.query(cmd)
        self.db.commit()

    def select(self, columns=None, conditions=None):
        """
        Selects the given columns from the table filtered by the conditions

        Keyword arguments:
        columns -- string of pattern: 'key, ..." or list of keys (Default: *)
        conditions -- string of pattern: 'key=value AND ...' (Default: nothing)
        """
        if not columns:
            columns = "*"
        elif type(columns) == list:
            columns = ",".join(columns)
        if not conditions:
            cmd = "SELECT {columns} FROM {name}"\
                .format(name=self.name,
                        columns=columns)
        else:
            cmd = "SELECT {columns} FROM {name} WHERE {conditions}"\
                .format(name=self.name,
                        columns=columns,
                        conditions=conditions)
        return(self.db.query(cmd))
