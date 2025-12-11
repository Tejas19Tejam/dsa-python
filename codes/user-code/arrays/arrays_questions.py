ar = [1, 2, 8, 4, 5, 6]

# Check if array is sorted
# def optimal_sol(ar):
#     i = 1
#     is_sorted = True
#     while i <= len(ar) - 1:
#         if not (ar[i - 1] <= ar[i]):
#             is_sorted = False
#             break
#         print(i)
#         i += 1

#     print("Is array sorted : ", is_sorted)

# optimal_sol(ar)


# Remove duplicates from a sorted array
dup_array = [1, 2, 2, 2, 3, 3, 4, 5]
#      i              j


def rem_duplicates(ar):
    i = 0
    j = 1
    while j < len(ar) - 1:
        if ar[i] == ar[j]:
            j += 1
        if ar[i] != ar[j]:
            ar[i + 1] = ar[j]
            i += 1

    print(ar)


rem_duplicates(dup_array)
