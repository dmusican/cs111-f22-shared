# Indefinite loop
# Checking for correctness, repeat if not correct

response = input("What's the best college? ")
while response != "carleton":
    print("Wrong, try again.")
    response = input("Again, what's the best college? ")
