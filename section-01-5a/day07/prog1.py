# Convert everything from lower case to upper
phrase = 'carleton'
for theLetter in phrase:
    unicodeValue = ord(theLetter)
    updatedValue = unicodeValue - 32
    updatedLetter = chr(updatedValue)
    print(updatedLetter)


