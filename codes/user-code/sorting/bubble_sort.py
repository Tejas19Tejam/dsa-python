# It pushes maximum to the last by adjacent swap

ar = [12, 2, 1, 45, 30, 90]


def bubble_sort(ar):
    for j in range(0, len(ar)):
        for i in range(0, len(ar) - j - 1):
            if ar[i] > ar[i + 1]:
                temp = ar[i + 1]
                ar[i + 1] = ar[i]
                ar[i] = temp
    print(ar)


bubble_sort(ar)
