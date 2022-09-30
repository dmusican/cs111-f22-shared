# Unnecessary, because len works
def getLength(phrase):
    total = 0
    for character in phrase:
        total = total + 1
    print("LENGTH IS", total, "!!!!")
    return total

print("length of dog is", getLength("dog"))
print("length of horse is", getLength("horse"))

