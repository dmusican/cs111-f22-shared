def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)


#print(fact(5))
#print(fact(7))

def mystery(n):
    if n == 1:
        return 2
    else:
        return 7 + mystery(n-1)

#print(mystery(3))


# Sum all items in a list
def sumup(items):
    if len(items) == 1:
        return items[0]   # first item
    else:
        return items[0] + sumup(items[1:])


#print(sumup([9, 2, 4, 3]))

# Check if a list is sorted. Return True if
# so, False if not
def checkSorted(items):
    if len(items) == 1:
        return True
    else:
        return items[0] < items[1] and checkSorted(items[1:])

print(checkSorted([3, 7, 11, 18, 21]))
print(checkSorted([12, 7, 11, 18, 21]))
