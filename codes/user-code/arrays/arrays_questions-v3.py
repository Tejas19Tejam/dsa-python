# Find the intersection of two sorted arrays
def brut_sol_q1(ar1, ar2):

    visited = [0 for i in range(len(ar2))]
    intersection = []
    i = 0

    for i in range(len(ar1)):
        for j in range(i + 1):
            if ar1[i] == ar2[j] and visited[j] != 1:
                intersection.append(ar1[i])
                visited.append(1)
                break
            if ar2[j] > ar1[i]:
                break

    print(intersection)


def optimal_sol_q1(ar1, ar2):
    intersection = []

    a1_len = len(ar1)

    i = 0
    j = 0

    while i < a1_len and j < len(ar2):
        if ar1[i] == ar2[j]:
            intersection.append(ar1[i])
            i += 1
            j += 1

        elif ar1[i] < ar2[j]:
            i += 1

        elif ar2[j] < ar1[i]:
            j += 1
    print(intersection)


# ar1 = [1, 2, 2, 3, 3, 4, 5, 6]
# ar2 = [2, 3, 3, 4, 5, 6, 6]
# brut_sol_q1(ar1, ar2)
# optimal_sol_q1(ar1, ar2)


# q2 :  Longest sub-array with sum K


def brut_sol_1_q2(ar, k1):
    length = 0
    for i in range(len(ar)):
        for j in range(i, len(ar)):
            sum1 = 0
            for k in range(i, j + 1):
                sum1 += ar[k]
            if sum1 == k1:
                length = max(length, j - i + 1)

    print(length)


# ar1 = [1, 2, 2, 3, 3, 4, 5, 6]
# ar2 = [2, 3, 3, 4, 5, 6, 6]
# brut_sol_1_q2(ar2, 8)


def brut_sol_2_q2(ar, sm):
    """Finds the length of the longest subarray with a given sum.
    This function uses a brute force approach to find the maximum length of a
    contiguous subarray whose elements sum to the target sum.
        ar (list): List of integers
        sm (int): Target sum to find in subarrays
        None: Prints the length of the longest subarray with sum equal to sm
    Time Complexity:
        O(n^2) - Two nested loops iterate through all possible subarrays
    Space Complexity:
        O(1) - Only uses a constant amount of extra space for variables
    """
    length = 0
    for i in range(len(ar)):
        s = 0
        for j in range(i, len(ar)):
            s += ar[j]
            if s == sm:
                length = max(length, j - i + 1)

    print(length)


# ar1 = [2, 3, 3, 4, 5, 6, 6]
# brut_sol_2_q2(ar1, 8)


def better_sol_q2(ar, k):
    pre_sum = 0
    max_len = 0
    ind_sum_hash = {}

    for i in range(len(ar)):
        pre_sum += ar[i]
        ind_sum_hash[i] = pre_sum
        # Check array from start till the current index giving you K
        if(ind_sum_hash == k):
            
            

    print(pre_sum, ind_sum_hash)


ar1 = [1, 5, 2, 4, 5, 9, 6]
better_sol_q2(ar1, 10)
