import numpy as np
from scipy.linalg import sqrtm
import sqlite3

class Recommender:
    def __init__(self, db):
        self.db = db.db

    def get_user_prefs(self):
        users = self.db.execute("SELECT DISTINCT username FROM users;").fetchall() 
        memes = self.db.execute("SELECT DISTINCT filename FROM memes;").fetchall()
        meme_idxs = {el[0]: i for i, el in enumerate(memes)}
        user_idxs = {el[0]: i for i, el in enumerate(users)}
        data_arr = []
        for user in user_idxs:
            user_arr = np.zeros(len(meme_idxs.keys()))
            user_memes = self.db.execute("SELECT meme, liked FROM users WHERE username=?", (user, )).fetchall()
            for meme, liked in user_memes:
                user_arr[meme_idxs[meme]] = 1 if liked else -1
            data_arr.append(np.array(user_arr))
        return meme_idxs, user_idxs, np.array(data_arr)

    def recommend(self, train, k=1):
        U, s, V = np.linalg.svd(train, full_matrices=False)
        s = np.diag(s)

        # top k
        s = s[0:k, 0:k]
        U = U[:, 0:k]
        V = V[0:k, :]

        s_root = sqrtm(s)

        Usk = U@s_root
        skV = s_root@V
        UsV = Usk@skV

        return UsV

