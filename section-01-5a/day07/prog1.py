# Convert everything from lower case to upper
phrase = 'carleton'
result = ""
caseShift = 32
for theLetter in phrase:
    unicodeValue = ord(theLetter)
    updatedValue = unicodeValue - caseShift
    updatedLetter = chr(updatedValue)
    result = result + updatedLetter
print(result)


