class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f'{self.name} is barking woof woof'


dog1 = Dog('bingo', 12)
print(dog1.bark())
print(f'{dog1.name} is {dog1.age} years old')