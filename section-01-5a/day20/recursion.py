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

def binarySearch(items, target):
    if len(items) == 0:
        return False    # didn't find it

    mid = len(items) // 2
    if items[mid] == target:
        return True
    elif items[mid] < target:
        return binarySearch(items[mid+1:], target)
    else:
        return binarySearch(items[:mid], target)

print(binarySearch([2, 9, 12, 15, 18], 15))
print(binarySearch([2, 9, 12, 15, 18], 17))
