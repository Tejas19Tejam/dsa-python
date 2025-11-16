# Find largest element in array

ar = [2, 2, 45, 12, 78, 2]


def find_large_elm(ar):
    largest = ar[0]

    for i in range(len(ar) - 1):
        if ar[i] > largest:
            largest = ar[i]
    print(largest)


find_large_elm(ar)
