from shapes.circle import Circle
from shapes.rectangle import Rectangle

def calArea(shape):
    print(shape.area())


rec = Rectangle(3, 4)
cir = Circle(5)

calArea(rec)
calArea(cir)