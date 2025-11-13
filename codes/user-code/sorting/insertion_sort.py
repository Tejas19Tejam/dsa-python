# Take an element and place it in its correct position

# average & worst time complexity is : O(N^2)
# BEST case time complexity : O(N)


ar = [12, 2, 1, 45, 30, 90]


def insertion_sort(ar):
    for i in range(0, len(ar)):
        j = i
        while j > 0 and ar[j - 1] > ar[j]:
            temp = ar[j - 1]
            ar[j - 1] = ar[j]
            ar[j] = temp
            j = j - 1
    print(ar)


insertion_sort(ar)
