infile = open('twocities.txt', 'r')
text = infile.read()
#print(text[:500])
#print(repr(text))
words = text.split()
for word in words:
    print(word)

