
# Don't need this because "len" is built-in
def getLength(flibble):
    total = 0
    for character in flibble:
        total = total + 1
    return total

print("Length of dog is", getLength("dog"))
print("Length of horse is", getLength("horse"))

