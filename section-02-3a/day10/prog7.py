# nested (wrapped inside)

x = 1
y = 3
if x == 1:
    if y == 3:
        print("A")
    else:
        print("B")
else:
    if y == 3:
        print("C")
    else:
        print("D")
