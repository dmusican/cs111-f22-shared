import numpy as np

def MergeSort(nums):
    # size of list?
    n = len(nums)

    # stopping case
    if n == 1:
        return

    # recursive case
    else:
        first = nums[:n // 2]
        second = nums[n // 2:]

        MergeSort(first)
        MergeSort(second)

        Merge(first, second, nums)



def Merge(l1, l2, l3):
    count1, count2, count3 = 0,0,0

    while count1 < len(l1) and count2 < len(l2):
        if l1[count1] < l2[count2]:
            l3[count3] = l1[count1]
            count1 = count1 + 1
        else:
            l3[count3] =  l2[count2]
            count2 = count2 + 1
        count3 = count3 + 1

    # empty out l1
    while count1 < len(l1):
        l3[count3] = l1[count1]
        count1 = count1 + 1
        count3 = count3 + 1

    # empty out l2
    while count2 < len(l2):
        l3[count3] = l2[count2]
        count2 = count2 + 1
        count3 = count3 + 1


def main():
    # size of list we are sorting
    size = 10
    # lower and upper limit on random numbers possible
    lower = 0
    upper = 100
    # get random list of numbers

    # Below is original code; since it is random, to duplicate the
    # problem that happened in class, I hardcoded in the numbers
    # from his demo
    #nums = np.random.randint(lower, upper, size)
    nums = np.array([7, 79, 37, 1, 64, 66, 29, 32, 49, 20])

    ##############################################################
    # The following line fixes the bug. Uncomment to see this.
    nums = nums.tolist()
    ##############################################################

    left = np.sort(np.random.randint(lower, upper, size // 2))
    right = np.sort(np.random.randint(lower, upper, size // 2))

    # combine both lists
    together = [*left, *right]

    # prints lists
    print('left: ', left)
    print('right: ', right)
    print('together:', together)
    print()

    print("left: ", left)
    print("right: ", right)
    print("together: ", together)
    print()

    # merge both
    Merge(left, right, together)
    print('merge ', together)
    print()

    # sort the list of nums
    MergeSort(nums)
    print(nums)

main()
