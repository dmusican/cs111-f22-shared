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

print(mystery(3))
