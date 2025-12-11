num = 56233


def extract_digits(num):

    rem_num = num

    while rem_num > 0:
        print(rem_num % 10)
        rem_num = int(rem_num / 10)


# extract_digits(num)


def digit_count(num):

    rem_num = num
    digit = 0

    while rem_num > 0:
        digit += 1
        rem_num = int(rem_num / 10)

    print("Digit count is : ", digit)


# digit_count(num)


def reverse_num(num):
    rev_num = 0
    rem_num = num

    while rem_num > 0:
        last_digit = rem_num % 10
        rem_num = int(rem_num / 10)
        rev_num = (rev_num * 10) + last_digit

    print(rev_num)

    return rev_num


# reverse_num(num)


def is_palindrome(num):
    rev_num = reverse_num(num)
    if rev_num == num:
        return True
    else:
        return False


# print(is_palindrome(121))
# print(is_palindrome(11156))


def is_armstrong_no(num):
    rem_num = num
    num_count = 0
    total_sum = 0

    # calculate count
    while rem_num > 0:
        num_count += 1
        rem_num = int(rem_num / 10)

    rem_num = num
    while rem_num > 0:
        last_digit = rem_num % 10
        total_sum = total_sum + (last_digit**num_count)
        rem_num = int(rem_num / 10)

    if total_sum == num:
        return True
    else:
        return False


print(is_armstrong_no(153))
print(is_armstrong_no(370))
