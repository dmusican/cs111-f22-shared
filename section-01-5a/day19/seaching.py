# Get words into a list
words = []
inpfile = open('twl06clean.txt', 'r')
for word in inpfile:
    words.append(word)
inpfile.close()
print(words)
