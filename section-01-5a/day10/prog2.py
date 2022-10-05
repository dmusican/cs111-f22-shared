# Piglatin translation
# if the word is not punctuation
word = input("What should I translate? ")

if len(word) == 5:
    output = word[1:] + word[0] + "ay"
    print(output)

print("Done!")
