import sqlite3
import json

class ImageNavigator:
    def __init__(self, image_dir, json_file, db):
        self.db = db.db
        self.image_dir = image_dir
        self.json_file = json_file
        self.image_data = self.load_image_data()
        self.seen_images = set()
        self.current_image_index = 0

    def add_meme(self, fname, tags):
        for tag in tags:
            self.db.execute("INSERT OR IGNORE INTO memes VALUES (?, ?);", (fname, tag))
        self.db.commit()


    def load_image_data(self):
        with open(self.json_file) as f:
            data = json.load(f)
            for fname, tags in data.items():
                self.add_meme(fname, tags)
            # print(self.db.execute("SELECT * FROM memes").fetchall())
            return data

    def mark_as_seen(self):
        filename = list(self.image_data.keys())[self.current_image_index]
        self.seen_images.add(filename)

    def find_next_unseen_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.image_data)
        while list(self.image_data.keys())[self.current_image_index] in self.seen_images:
            self.current_image_index = (self.current_image_index + 1) % len(self.image_data)
        return list(self.image_data.keys())[self.current_image_index]

