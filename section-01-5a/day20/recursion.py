# Working on recursion
def fact(n):
    # base case
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

#print(fact(3))

def mystery(n):
    if n == 1:
        return 2
    else:
        return 7 * mystery(n-1)

#print(mystery(3))

# Add all items in a list
def sumup(items):
    if len(items) == 1:
        return items[0]   # first item
    else:
        return items[0] + sumup(items[1:])

#print(sumup([2, 9, 4, 3, 7]))

# Check to see if a list is sorted
# return True or False
def checkSorted(items):
    if len(items) == 1:
        return True
    else:
        return items[0] < items[1] and \
               checkSorted(items[1:])
