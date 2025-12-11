# Left Rotate an array by one place


# ar = [1, 2, 3, 4, 5, 6, 7]


def brut_sol_q1(ar):
    temp = ar[0]

    for i in range(len(ar) - 1):
        ar[i] = ar[i + 1]

    ar[-1] = temp
    print(ar)


# Left Rotate an array by d positions
ar_q2 = [1, 2, 3, 4, 5, 6, 7, 8]


def brut_sol_q2(arr, places):

    # extract elements upto given position
    no_of_rotations = places % len(ar)
    extract_no = []

    for i in range(no_of_rotations):
        extract_no.append(arr[i])

    for j in range(len(extract_no), len(arr)):
        arr[j - no_of_rotations] = arr[j]

    print(extract_no)
    # Placing

    k = 0
    for i in range(len(arr) - no_of_rotations, len(arr)):
        arr[i] = extract_no[k]
        k += 1

    print(arr)


def optimal_sol_q2(arr, d):
    temp = arr[0:d]
    temp2 = arr[d : len(arr)]

    temp.reverse()
    temp2.reverse()

    print(temp2 + temp)


# optimal_sol_q2(ar_q2, 3)


# Move all zeros to the end of array

arr_q3 = [1, 0, 2, 4, 0, 0, 3, 0, 8, 6]
# arr_q3 = [0, 0, 0, 0, 0, 0, 0]


# def brut_sol_q3(ar):
#     num_arr = []
#     zero_count = 0

#     for i in range(len(ar)):
#         if ar[i] != 0:
#             num_arr.append(ar[i])
#         else:
#             zero_count += 1

#     while zero_count > 0:
#         num_arr.append(0)
#         zero_count -= 1

#     print(num_arr)


def brut_sol_q3(ar):
    num_arr = []

    for i in range(len(ar)):
        if ar[i] != 0:
            num_arr.append(ar[i])

    for j in range(len(ar)):
        if j < len(num_arr):
            ar[j] = num_arr[j]
        else:
            ar[j] = 0

    print(ar)


# brut_sol_q3(arr_q3)


def optimal_sol_q3(ar):
    # Find first zero number
    j = -1  # stores index of first zero number
    for i in range(len(ar)):
        if ar[i] == 0:
            j = i
            break

    if j == -1:
        return ar

    # find index of non-zero numbers after jth , and swap

    for k in range(j + 1, len(ar)):
        if ar[k] != 0:
            temp = ar[k]
            ar[k] = ar[j]
            ar[j] = temp
            j += 1
        else:
            continue
    print("ANS", ar)


# print("ORG", arr_q3)
# optimal_sol_q3(arr_q3)


# Union of two sorted array

arr_q4 = [1, 3, 5, 8, 9]
arr_q4_1 = [5, 9, 12, 15, 18]

# Using set data structure
def brut_sol_q4(ar1, ar2):
    set2 = set()
    union = []
    for i in ar1:
        if i not in set2:
            set2.add(i)
    for j in ar2:
        if j not in set2:
            set2.add(j)

    for elm in set2:
        union.append(elm)

    print(union)


# brut_sol_q4(arr_q4, arr_q4_1)

def optimal_sol_q4(ar1 , ar2):
    # declare a pointers
    i=0
    j=0

    union=[]

    ar1_len = len(ar1)
    ar2_len = len(ar2)

    while i < ar1_len and j < ar2_len:
        if ar1[i] <= ar2[j]:
            if ar1[i] not in union:
                union.append(ar1[i])
            i+=1
        elif ar2[j] <= ar1[i]:
            if ar2[j] not in union:
                union.append(ar2[j])
            j+=1

    while i < ar1_len:
        if ar1[i] not in union:
            union.append(ar1[i])
        i += 1
    while j < ar2_len:
        if ar2[j] not in union:
            union.append(ar2[j])
        j += 1

    print(union)



optimal_sol_q4([1,1,2,3,4,5], [2,3,4,4,5,6])



