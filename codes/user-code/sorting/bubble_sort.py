# It pushes maximum to the last by adjacent swap

ar = [12, 2, 1, 45, 30, 90]


# Worst case Time Complexity : O(n^2)
def bubble_sort(ar):
    for j in range(0, len(ar)):
        for i in range(0, len(ar) - j - 1):
            if ar[i] > ar[i + 1]:
                temp = ar[i + 1]
                ar[i + 1] = ar[i]
                ar[i] = temp
    print(ar)


# We can make a optimization lets  say you are given an array if already sorted


ar1 = [1, 2, 3, 4, 5, 6]  # sorted array


def optimized_bubble_sort(ar):
    for i in range(0, len(ar)):
        isSwapped = False
        print("Done")
        for j in range(0, (len(ar) - i) - 1):
            if ar[j] > ar[j + 1]:
                temp = ar[j + 1]
                ar[j + 1] = ar[j]
                ar[j] = temp
                isSwapped = True
        if not isSwapped:
            print("O")
            break


# bubble_sort(ar)
optimized_bubble_sort(ar1)

# The time complexity of optimized one is O(N)
