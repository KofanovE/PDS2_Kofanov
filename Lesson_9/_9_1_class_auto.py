class ClassAuto:

    def __init__(self, brand, color, capacity):
        self.brand = brand
        self.color = color
        self.capacity = capacity

    def moving_forward(self):
        return "is moving forward"

    def moving_revers(self):
        return "is moving revers"



car_1 = ClassAuto('toyota', 'metalic', 1.8)
print(f'brand: {car_1.brand}, color: {car_1.color}, engine capacity: {car_1.capacity}')
print(f'{car_1.brand} {car_1.moving_forward()}')



class AutoMod(ClassAuto):

    def __init__(self, brand, color, capacity):
        ClassAuto.__init__(self, brand, color, capacity)

    def moving_right(self):
            return "is moving right"

    def moving_left(self):
            return "is moving left"


car_2 = AutoMod('bmv', 'black', 3.0)
print(f'{car_2.color} {car_2.brand} {car_2.moving_right()}')