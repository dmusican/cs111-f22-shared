# Number guessing game
secret = 37
guess = int(input("What is your guess?"))
while guess != secret:
    if guess < secret:
        print("Too small, friend, try again.")
    elif guess > secret:
        print("Too big, my special friend, go again.")
    else:
        print("Got it")
