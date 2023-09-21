import random
import string

class RandomWordGenerator:
    def __init__(self, length=8):
        self.length = length

    def generate_random_word(self):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(self.length))
