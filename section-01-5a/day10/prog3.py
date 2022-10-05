# Piglatin translation
# if the word is not punctuation
# don't translate
# if starts with a vowel, leave it there
word = input("What should I translate? ")

if word == "?":
    output = word
else:
    output = word[1:] + word[0] + "ay"

print(output)
