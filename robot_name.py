import random
import string


class Robot:
    def __init__(self):
        self.name = self.generate_name()

    def generate_name(self):
        name = ""
        for i in range(0, 2):
            name += random.choice(string.ascii_uppercase)
        for i in range(0, 3):
            name += str(random.randint(0, 9))
        return name

    def reset(self):
        random.seed()
        self.__init__()
