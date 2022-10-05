# Translation to Piglatin, again
# Only translate if no punctuation,
# but also if starts with a vowel, leave
# it there
word = input("Give me a word: ")
if word in ['?', '!', ',']:
    output = word
elif word[0] in ['a', 'e', 'i', 'o', 'u']:
    output = word + "ay"
else:
    output = word[1:] + word[0] + "ay"

#######
if 3 == 5:
    print("pigs can fly")
else:
    print("pigs cannot fly")


print("Result is ", output)
