ar = [23, 12, 3]

# Time complexity  = O(N^2)


def selection_sort(ar):
    sorted_arr = ar
    min_value = 0
    for ind in range(0, len(sorted_arr) - 1):
        for i in range(ind, len(sorted_arr)):
            if ar[i] < sorted_arr[min_value]:
                min_value = i

        temp = sorted_arr[ind]
        sorted_arr[ind] = sorted_arr[min_value]
        sorted_arr[min_value] = temp

    print(sorted_arr)


selection_sort(ar)
