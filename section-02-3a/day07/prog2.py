# Shift from to lower to upper case
# (There's an easier way, but I want
# to show this works)
phrase = 'carleton'
for letter in phrase:
    unicodeValue = ord(letter)
    newValue = unicodeValue - 32
    newLetter = chr(newValue)
    print(newLetter, end="")
print()