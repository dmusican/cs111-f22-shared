infile = open('twocities.txt', 'r')
# Get all of the file into one string
text = infile.read()

# Get a list of all the words in that string
words = text.split()
for word in words:
    piglatin = word[1:] + word[0] + "ay"
    print(piglatin)
