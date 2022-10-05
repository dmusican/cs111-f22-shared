# Piglatin translation
# if the word is not punctuation
word = input("What should I translate? ")

if word == "?":
    output = word
else:
    output = word[1:] + word[0] + "ay"

print(output)
