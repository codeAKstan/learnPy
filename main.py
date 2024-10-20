import random

number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess the number: "))
        if guess > number:
            print("Your guess is too high.")
        elif guess < number:
            print("Your guess is too low.")
        else:
            print("Correct! The number was", number)
            break
    except ValueError:
        print("Please enter a valid number.")
