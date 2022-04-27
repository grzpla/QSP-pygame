

class Entry(object):
    def __init__(self, screen, text="input.", rect=(0, 0, ), bg_color='white', color='black'):
        self.x, self.y, self.width, self.height = rect

        self.typing = False

    def display(self):
        pass
