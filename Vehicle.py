class Vehicle(object):
    def __init__(self, color=None, speed=0, tires=4, mpg=0, capacity=0):
        print('In --init-- (2)')
        self.color = None
        self.max_speed = 0
        self.num_tires = 0
        self.mpg = 0


    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_mpg(self, mpg):
        self.mpg = mpg

    def get_mpg(self):
        return self.mpg

    def display(self):
        print(f'color: {self.color} max_speed: {self.max_speed} tires: {self.num_tires} mpg: {self.mpg}')
# extined
class car(Vehicle):
    def __init__(self, capacity):
    super().__init__(self, capacity=)

# Not in object
if __name__ == '__main__':
    v1 = Vehicle('Blue', 90, 4, 35)
    v2 = Vehicle('REd', 150, 4, 15)
    v3 = Vehicle('Green')
    v4 = Vehicle()
    v5 = car(7)

    print(v5.seating_capacity())

    v1.display()
    v2.display()
    v3.display()
