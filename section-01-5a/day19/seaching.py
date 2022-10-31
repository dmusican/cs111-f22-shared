def linearSearch(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i   # location where I found it
    return -1    # -1 means didn't find

def binarySearch(items, target):
    low = 0
    high = len(items)-1

    while low <= high:
        mid = (low + high)//2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1    # didn't find it

# Get words into a list
words = []
inpfile = open('twl06clean.txt', 'r')
for word in inpfile:
    words.append(word.strip())
inpfile.close()

print("Linear")
for i in range(100):
    linearSearch(words, 'zymometer')
    linearSearch(words, 'zymometushlkfhgf')
print("Binary")
for i in range(100):
    binarySearch(words, 'zymometer')
    binarySearch(words, 'zymometushlkfhgf')
print("Done")
