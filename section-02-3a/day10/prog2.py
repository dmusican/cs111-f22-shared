# Translation to Piglatin, again
# Only translate if no punctuation,
# otherwise leave intact
word = input("Give me a word: ")
if len(word) == 5:
    output = word[1:] + word[0] + "ay"
    print(output)

print("Done!")
