# Number guessing game
secret = 37

guess = -1  # ensures while gets started
while guess != secret:
    guess = int(input("What is your guess?"))
    if guess < secret:
        print("Too small, friend, try again.")
    elif guess > secret:
        print("Too big, my special friend, go again.")

print("Got it")
