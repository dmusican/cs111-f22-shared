import random

def merge(array, tempArray, leftStart, rightStart, rightEnd):
    leftEnd = rightStart - 1
    temp = 0
    left = leftStart
    right = rightStart

    # Start merging until one of the halves is exhausted
    while left <= leftEnd and right <= rightEnd:
        if array[left] <= array[right]:
            tempArray[temp] = array[left]
            left += 1
        else:
            tempArray[temp] = array[right]
            right += 1
        temp += 1
    
    # Copy rest of first half
    while left <= leftEnd:
        tempArray[temp] = array[left]
        temp += 1
        left += 1

    # Copy rest of second half
    while right <= rightEnd:
        tempArray[temp] = array[right]
        temp += 1
        right += 1
    
    # Copy temp array over original array
    for i in range(rightEnd - leftStart + 1):
        array[leftStart+i] = tempArray[i]

def mergeSort(array, tempArray, left, right):
    if left < right:
        center = (left + right) // 2
        mergeSort(array, tempArray, left, center)
        mergeSort(array, tempArray, center+1, right)
        merge(array, tempArray, left, center+1, right)

def mergeSortStarter(array):
    tempArray = [0]*len(array)
    mergeSort(array, tempArray, 0, len(array)-1)

def merge(array, tempArray, leftStart, rightStart, rightEnd):
    leftEnd = rightStart - 1
    temp = 0
    left = leftStart
    right = rightStart

    # Start merging until one of the halves is exhausted
    while left <= leftEnd and right <= rightEnd:
        if array[left] <= array[right]:
            tempArray[temp] = array[left]
            left += 1
        else:
            tempArray[temp] = array[right]
            right += 1
        temp += 1

    # Copy rest of first half
    while left <= leftEnd:
        tempArray[temp] = array[left]
        temp = temp + 1
        left = left + 1

    # Copy rest of second half
    while right <= rightEnd:
        tempArray[temp] = array[right]
        temp = temp + 1
        right = right + 1

    # Copy temp array over original array

    for i in range(rightEnd-leftStart+1):  # num items merged
       array[leftStart + i] = tempArray[i]

def shuffle(items):
    random.seed(55057)
    for i in range(1000000):
        spot1 = random.randrange(len(items))
        spot2 = random.randrange(len(items))
        (items[spot1], items[spot2]) = (items[spot2], items[spot1])
    
def main():
    size = 50000
    items = list(range(size))
    shuffle(items)
    print("Original list (portion):")
    print(items[:100])
    print("Sorted items (portion):")
    mergeSortStarter(items)
    print(items[:100])

    for i in range(len(items)):
        if items[i] != i:
            print("Error in sorting.")
            exit(1)

if __name__=="__main__":
    main()
