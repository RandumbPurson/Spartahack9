class User:
    def __init__(self) -> None:
        self.liked = []
        self.disliked = []

    def updatePrefs(self, res):
        if res.liked:
            self.liked.append(res.img)
        else:
            self.disliked.append(res.img)

