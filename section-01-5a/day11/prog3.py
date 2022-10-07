# Guessing game
# Computer picks a number, user has to guess it
import random

secret = random.randrange(100) + 1

guess = -1   # priming value
while guess != secret:
    guess = int(input("What's your guess? "))
    if guess < secret:
        print("Too small, my friend, try again.")
    elif guess > secret:
        print("Alas your guess is too mighty. Try again.")
    else:
        print("You got it!")
