import json

class ImageNavigator:
    def __init__(self, image_dir, json_file):
        self.image_dir = image_dir
        self.json_file = json_file
        self.image_data = self.load_image_data()
        self.seen_images = set()
        self.current_image_index = 0

    def load_image_data(self):
        with open(self.json_file) as f:
            return json.load(f)

    def mark_as_seen(self):
        filename = list(self.image_data.keys())[self.current_image_index]
        self.seen_images.add(filename)

    def find_next_unseen_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.image_data)
        while list(self.image_data.keys())[self.current_image_index] in self.seen_images:
            self.current_image_index = (self.current_image_index + 1) % len(self.image_data)
        return list(self.image_data.keys())[self.current_image_index]

