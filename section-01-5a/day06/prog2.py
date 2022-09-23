things = [1, 9, "dave", "friday"]
word = "carleton"
print(type(things))
print(type(word))
print("first:", things[0])
print("last:", things[-1])
print("middleish:", things[1:3])

print("It's coming....")
for something in things[1:3]:
    print(something)

things[1] = 25
print(things)