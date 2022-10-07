# Guessing game
# Computer picks a number, user has to guess it

secret = 37

while guess != secret:
    guess = int(input("What's your guess? "))
    if guess < secret:
        print("Too small, my friend, try again.")
    elif guess > secret:
        print("Alas your guess is too mighty. Try again.")
    else:
        print("You got it!")
