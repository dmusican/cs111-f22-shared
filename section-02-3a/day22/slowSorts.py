import random

def selectionSort(items):   
    for i in range(len(items)):
        smallestPos = i
        for j in range(i+1, len(items)):
            if items[j] < items[smallestPos]:
                smallestPos = j
        (items[smallestPos], items[i]) = (items[i], items[smallestPos])


def insertionSort(items):
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j-1] > items[j]:
            (items[j], items[j-1]) = (items[j-1], items[j])
            j -= 1

def insertionSortOptimized(items):
    for i in range(1, len(items)):
        j = i
        swapVal = items[i]
        while j > 0 and items[j-1] > swapVal:
            (items[j], items[j-1]) = (items[j-1], items[j])
            j -= 1
        items[j] = swapVal

def shuffle(items):
    random.seed(55057)
    for i in range(1000000):
        spot1 = random.randrange(len(items))
        spot2 = random.randrange(len(items))
        (items[spot1], items[spot2]) = (items[spot2], items[spot1])

def main():
    random.seed(90125)
    items = [0]*5000
    for i in range(len(items)):
        items[i] = i
    shuffle(items)
    print("Original list (portion):")
    print(items[:100])
    print("Sorted items (portion):")
    selectionSort(items)
    print(items[:100])

    for i in range(len(items)):
        if items[i] != i:
            print("Error in sorting.")
            exit(1)

if __name__=="__main__":
    main()
