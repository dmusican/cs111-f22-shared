# Searching in dictionaries is faster
# than lists
size = 2000
print("Trying dictionary")
dict = {}
for i in range(size):
    dict[i] = i

matches = 0
for i in range(size):
    if i in dict:   # test to see if key is in dict
        matches = matches + 1
print(matches)

print("Trying list")
items = []
for i in range(size):
    items.append(i)

matches = 0
for i in range(size):
    if i in items:
        matches = matches + 1
print(matches)
