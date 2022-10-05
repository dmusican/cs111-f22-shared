# Piglatin translation
# only if the length of word is 5
word = input("What should I translate? ")

if len(word) == 5:
    output = word[1:] + word[0] + "ay"
    print(output)

print("Done!")
