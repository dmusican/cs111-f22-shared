
# Don't need this because "len" is built-in
def getLength(phrase):
    total = 0
    for character in phrase:
        total = total + 1
    return total

print("Length of dog is", getLength("dog"))
print("Length of horse is", getLength("horse"))

