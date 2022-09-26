# Shift from to lower to upper case
# (There's an easier way, but I want
# to show this works)
phrase = 'carleton[]'
shift = ord('a') - ord('A')
answer = ""
for symbol in phrase:
    unicodeValue = ord(symbol)
    newValue = unicodeValue - shift
    newLetter = chr(newValue)
    answer = answer + newLetter
print(answer)