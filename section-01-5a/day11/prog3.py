# Guessing game
# Computer picks a number, user has to guess it

secret = 37

guess = int(input("What's your guess? "))

while guess != secret:
    if guess < secret:
        print("Too small, my friend, try again.")
        guess = int(input("What's your guess? "))
    elif guess > secret:
        print("Alas your guess is too mighty. Try again.")
        guess = int(input("What's your guess? "))
    else:
        print("You got it!")
