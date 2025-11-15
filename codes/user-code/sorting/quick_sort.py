# Quick Sort using Hoare Partition Scheme

# Quick sort has time complexity similar to merge sort but dosen't use the extra space i.t 0(1)


# Algorithm Steps:

# 1. Pickup a pivot & place it in its correct place in the sorted array
# 2. all Smaller or equal value then pivot on the left and greater on the right


# Terms :
# Pivot = can be any element, from array


# Time complexity : n * log(N)
# Space complexity : 0(1)

ar = [23, 12, 3, 56, 1, 30]


def quick_sort(ar, low, high):
    if low < high:

        # Find Pivot
        pivot = ar[low]

        # Create two pointers and place it in start and end of array
        i = low
        j = high

        while i < j:

            # Check if ith value is grater then pivot and jth value is smaller than pivot

            while ar[i] <= pivot and i <= high - 1:
                i += 1

            while ar[j] > pivot and j >= low + 1:
                j -= 1

            if i < j:
                # swap both
                temp = ar[i]
                ar[i] = ar[j]
                ar[j] = temp

        # Once j < i (cross each other) . SWAP low value and jth value

        t1 = ar[j]
        ar[j] = pivot
        ar[low] = t1

        # Create a partition index
        partition_ind = j

        # Sort the arrays which is on the left and right side of partition_ind using recursion
        quick_sort(ar, low, partition_ind - 1)
        quick_sort(ar, partition_ind + 1, high)

    print(ar)


quick_sort(ar, 0, len(ar) - 1)
