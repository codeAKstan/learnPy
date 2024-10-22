class Animal:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def sound(self):
        return "some sound"

class Dog(Animal):
    def sound(self):
        return "bark"


dog = Dog("bingo")
print(dog.sound())