class User:
    def __init__(self, db) -> None:
        self.db = db

    def login(self, username):
        self.username = username

    def updatePrefs(self, res):
        if self.username is None:
            return "500"
        self.db.execute("INSERT INTO users VALUES (?, ?, ?)", (self.username, res["img"], res["liked"]))
        print(self.db.execute("SELECT * FROM users").fetchall())
        return "200"

