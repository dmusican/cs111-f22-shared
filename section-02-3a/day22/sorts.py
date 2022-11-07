
def shuffle(items):
    random.seed(55057)
    for i in range(1000000):
        spot1 = random.randrange(len(items))
        spot2 = random.randrange(len(items))
        (items[spot1], items[spot2]) = \
            (items[spot2], items[spot1])

def main():
    random.seed(90125)
    items = [0]*5000
    for i in range(len(items)):
        items[i] = i
    shuffle(items)
    print("Original list (portion):")
    print(items[:100])
    print("Sorted items (portion):")
    insertionSort(items)
    print(items[:100])

    for i in range(len(items)):
        if items[i] != i:
            print("Error in sorting.")
            exit(1)

if __name__=="__main__":
    main()
