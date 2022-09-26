# Convert everything from lower case to upper
phrase = 'carleton'
result = ""
for theLetter in phrase:
    unicodeValue = ord(theLetter)
    updatedValue = unicodeValue - 32
    updatedLetter = chr(updatedValue)
    result = result + updatedLetter
print(result)


