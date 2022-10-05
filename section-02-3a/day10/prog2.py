# Translation to Piglatin, again
# Only translate if no punctuation,
# otherwise leave intact
word = input("Give me a word: ")
if word == '?':
    output = word

else:
    output = word[1:] + word[0] + "ay"


if 3 == 5:
    print("pigs can fly")
else:
    print("pigs cannot fly")


print("Result is ", output)
