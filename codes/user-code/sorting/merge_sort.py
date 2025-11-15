import math

# Insertion sort, selection sort and quick sort takes a O(n^2) time complexity to solve a problem
# But merge sort is a much more optimized algorithm


# Introduction about merge sort
# The main concept of algorithm : DIVIDE AND MERGE


# Time complexity worst case is : O(N * log N )
# Space complexity worst case is : O(N)


def merge_sort(ar, low, high):

    # Base condition
    if low >= high:
        return

    # Middle index
    middle_idx = math.floor((low + high) / 2)

    # Create a sort Left side array of hypothetically divided array
    # LEFT
    merge_sort(ar, low, middle_idx)
    # RIGHT
    merge_sort(ar, middle_idx + 1, high)

    p1 = low
    p2 = middle_idx + 1
    temp = []

    while p1 <= middle_idx and p2 <= high:
        if ar[p1] <= ar[p2]:
            temp.append(ar[p1])
            p1 += 1
        else:
            temp.append(ar[p2])
            p2 += 1

    # Copy remaining elements, if any
    while p1 <= middle_idx:
        temp.append(ar[p1])
        p1 += 1
    while p2 <= high:
        temp.append(ar[p2])
        p2 += 1

    for i in range(len(temp)):
        ar[low + i] = temp[i]
    print(temp)
    print(ar)


merge_sort([12, 45, 21, 2], 0, 3)
