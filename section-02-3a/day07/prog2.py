# Shift from to lower to upper case
# (There's an easier way, but I want
# to show this works)
phrase = 'carleton'
shift = ord('a') - ord('A')
for letter in phrase:
    unicodeValue = ord(letter)
    newValue = unicodeValue - shift
    newLetter = chr(newValue)
    print(newLetter, end="")
print()