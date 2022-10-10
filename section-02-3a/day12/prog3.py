
response = input("Favorite color?")
# if response != "blue" and response != "green":
# if not (response == blue)  and  not (response == green)
# DeMorgan's Laws (one of them)
if not (response == "blue" or response == "green"):
    print("Me too!")
