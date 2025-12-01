
import random

number = random.randint(1, 20)

while True:
    guess = int(input("Guess a number between 1 and 20: "))

    if guess == number:
        print("correct guess!")

    elif guess < number:
        print("Too low")
    
    else:
        print("Too high")