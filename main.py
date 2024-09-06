#  classses and objects
class Dog:

    specie = "canis domestica"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def description(self):
        return f'my name is {self.name}, im a {self.age} years old'
    
    @classmethod
    def whatspecie(cls):
        return f'I belong to the specie {cls.specie}'
class Labrodor(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
my_dog = Dog('bingo', 22)
my_lab = Labrodor("bunny", 23, "pink")

print(my_lab.color)
print(my_lab.whatspecie())
print(my_lab.description())