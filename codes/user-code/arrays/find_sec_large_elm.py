ar_neg = [-8, -3, -4, -7, -10]
ar = [8, 3, 4, 7, 10]


# OPTIMAL
# This works for both types of array (neg or positive)
def optimal_sol(ar):
    second_elm = float("-inf")
    first = ar[0]

    for i in range(len(ar)):
        if ar[i] < first and ar[i] > second_elm:
            second_elm = ar[i]
        if ar[i] > first:
            second_elm = first
            first = ar[i]

    print(second_elm)


optimal_sol(ar)


# Find the second largest and second smallest element in array
ar2 = [6, 2, 8, 4, 9, 5]


def optimal(ar):
    sec_small = float("-inf")
    sec_large = float("inf")

    large = ar[0]
    small = ar[0]

    for i in range(len(ar)):
        # Second smallest
        if ar[i] != small and ar[i] < sec_small:
            sec_small = ar[i]
        if ar[i] < small:
            sec_small = small
            small = ar[i]

    for i in range(len(ar)):
        # second larger
        if ar[i] > large:
            sec_large = large
            large = ar[i]
        if ar[i] > large and ar[i] > sec_large:
            sec_large = ar[i]

    print("Second Large", sec_large)
    print("Second small", sec_small)


optimal(ar2)
