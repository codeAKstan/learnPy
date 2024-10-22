class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @staticmethod
    def start():
        return "car is starting"

    def info(self):
        return f'make is {self.make}, with model {self.model} made in the year {self.year}'


car = Car('mercedes', 'glk', 2014)
print(car.start())
print(car.info())