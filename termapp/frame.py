from termapp.formatstring import FormatString

class Frame:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.lines = []

    def set_lines(self, lines):
        for line in lines:
            pass