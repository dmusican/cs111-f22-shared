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
