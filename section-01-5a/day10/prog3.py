# Piglatin translation
# if the word is not punctuation
# don't translate
# if starts with a vowel, leave it there

word = input("What should I translate? ")

if word in ["?", "!", ","]:
    output = word


if word[0] in ["a", "e", "i", "o", "u"]:
    output = word + "ay"
else:
    output = word[1:] + word[0] + "ay"

print(output)
