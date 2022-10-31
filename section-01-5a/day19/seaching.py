def linearSearch(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i   # location where I found it
    return -1    # -1 means didn't find


# Get words into a list
words = []
inpfile = open('twl06clean.txt', 'r')
for word in inpfile:
    words.append(word.strip())
inpfile.close()

print(linearSearch(words, 'zymometer'))
print(linearSearch(words, 'zymometushlkfhgf'))
