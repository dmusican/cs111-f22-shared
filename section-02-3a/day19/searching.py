def linearSearch(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i  # location where found

    return -1   # not found

words = []
inpfile = open('twl06clean.txt', 'r')
for word in inpfile:
    words.append(word.strip())
inpfile.close()


print(linearSearch(words, 'zymometer'))
