# Number guessing game
secret = 37
guess = int(input("What is your guess?"))
while guess != secret:
    if guess < secret:
        print("Too small, friend, try again.")
        guess = int(input("What is your guess?"))
    elif guess > secret:
        print("Too big, my special friend, go again.")
        guess = int(input("What is your guess?"))
    else:
        print("Got it")
