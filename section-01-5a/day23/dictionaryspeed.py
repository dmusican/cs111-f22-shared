
size = 20000

print("Trying dictionary")
itemsdict = {}
for i in range(size):
    itemsdict[i] = i

matches = 0
for i in range(size):
    if i in itemsdict:     # if it is a key
        matches += 1
print(matches)

print("Trying list")
itemslist = []
for i in range(size):
    itemslist.append(i)

matches = 0
for i in range(size):
    if i in itemslist:
        matches += 1
print(matches)
