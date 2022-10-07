# indefinite loop
# Keep asking a question until get the right answer
response = input("What's the best college? ")
while response != "carleton":
    print("Wrong answer, try again.")
    response = input("Really, what's the best college? ")
print("Finally.")
