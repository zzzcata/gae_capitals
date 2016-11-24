from random import randint

class Capital(object):
    def __init__(self, name, pictures):
        # type: (object, object) -> object
        self.name = name
        self.pictures = pictures

    def guess(self, guess_name):
        return self.name.lower() == guess_name.lower()

    def get_rand_img_url(self):
        rn = randint(0, len(self.pictures)-1)
        return self.pictures[rn]