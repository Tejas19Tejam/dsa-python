# Print name N times using Recursion

# def print_name_n_times(n, count):
#   if count == n:
#     return 0
#   else:
#     print("Name", "Vasudev", count)
#     print_name_n_times(n, count + 1)

# print_name_n_times(5, 0)

# Print Linearly from 1 to N

# def print_from_1_N(digit, n):

#   if digit > n:
#     return 0
#   else:
#     print("Digit", digit)
#     print_from_1_N(digit + 1, n)

# print_from_1_N(1, 10)

# Print 1 to N (Using backtracking)

# def print_1_to_N(i, n):
#   if i < 1:
#     return 0
#   else:
#     print_1_to_N(i - 1, n)
#     print(i)

# n = 3
# print_1_to_N(n, n)

# Print N to 1 (Using backtracking)

# def print_N_to_1(i, n):
#   if i > n:
#     return 0
#   else:
#     print_N_to_1(i + 1, n)
#     print(i)

# print_N_to_1(1, 3)

# Sum of first N numbers using recursion

# def sum_of_n(n):
#   if n == 0:
#     return 0
#   else:
#     return n + sum_of_n(n - 1)

# total_sum = sum_of_n(4)
# print(total_sum)

# Factorial of first N numbers using recursion

# def fact_of_n(n):
#   if n == 0:
#     return 1
#   else:
#     return n * fact_of_n(n - 1)

# total = fact_of_n(4)
# print(total)

# Reverse an array using recursion

# arr = [1, 2, 3, 4, 5, 6, 7]

# def reverse_array(start, end, arr):
#   if start >= end:
#     return arr
#   else:
#     temp = arr[start]
#     arr[start] = arr[end]
#     arr[end] = temp
#     return reverse_array(start + 1, end - 1, arr)

# reversed_arr = reverse_array(0, len(arr) - 1, arr)
# print(reversed_arr)

# Check if a given string is palindrome or not using recursion

# def is_str_palindrome(i, s):
#   # Base case: reached or passed the middle
#   if i >= len(s) // 2:
#     return True

#   # If mismatch found
#   if s[i] != s[len(s) - i - 1]:
#     return False

#   # Recursive call
#   return is_str_palindrome(i + 1, s)

# print(is_str_palindrome(0, "tetaet"))

# 0 1 1 2   5 8 .......


# Problem : Find the nth place Fibonaci number using recursion (TC -> 2 ^ N)
def nth_fibonaci_number(n):
    if n <= 1:
        return n
    else:
        return nth_fibonaci_number(n - 1) + nth_fibonaci_number(n - 2)


print(nth_fibonaci_number(4))
