
class Parallelogram:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self): # Площа паралелограма з прямим кутом = ширина * довжину
        return self.width * self.length


class Square(Parallelogram):

    def __init__(self, width):
        self.width = width
        self.length = width


a = Square(3)
print(f'\nПлоща квадрата зі стороною {a.width} дорівнює {a.get_area()}')


