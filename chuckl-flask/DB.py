import sqlite3

class DB:
    def __init__(self, fname) -> None:
        self.db = sqlite3.connect(fname, check_same_thread=False)
        self.init_tables()

    def init_tables(self):
        if not self.table_exists("memes"):
            self.db.execute("CREATE TABLE memes(filename, tag, UNIQUE(filename, tag));")
        if not self.table_exists("users"):
            self.db.execute("CREATE TABLE users(username, meme, liked);")

    def table_exists(self, table):
        res = self.db.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name=?;", (table, ))
        return len(res.fetchall())
