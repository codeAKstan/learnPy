class Animal:
    @staticmethod
    def make_sound():
        print("Animal sound")


class Dog(Animal):
    def make_sound(self):
        print("bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

animal = Animal()
dog = Dog()
cat = Cat()

cat.make_sound()
dog.make_sound()
animal.make_sound()