import math
class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return f'the area of a circle with radius {self.r} is {math.pi * self.r * self.r}'

