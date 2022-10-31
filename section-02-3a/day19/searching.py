def linearSearch(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i  # location where found

    return -1   # not found

def binarySearch(items, target):
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high)//2
        if target == items[mid]:
            return mid
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

words = []
inpfile = open('twl06clean.txt', 'r')
for word in inpfile:
    words.append(word.strip())
inpfile.close()

scale = 100
print("Linear")
for i in range(scale):
    linearSearch(words, 'zymometer')
    linearSearch(words, 'blahblahblah')

print("Binary")
for i in range(scale):
    binarySearch(words, 'zymometer')
    binarySearch(words, 'blahblahblah')

print("Done")
