class Bird:
    def speak(self):
        return f'Chirp'
    
class Duck(Bird):
    def speak(self):
        return f'quack'
    
def bird_speak(animal):
    print(animal.speak())

my_bird = Bird()
my_duck = Duck()

bird_speak(my_bird)
bird_speak(my_duck)