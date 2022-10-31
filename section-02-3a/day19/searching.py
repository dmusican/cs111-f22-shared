words = []
inpfile = open('twl06clean.txt', 'r')
for word in inpfile:
    words.append(word.strip())
inpfile.close()

print(words)
