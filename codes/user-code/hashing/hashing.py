# Hashing

ar = [1, 2, 3, 4, 45, 56, 3, 4, 45, 56]


def find_count(arr):
    hash = {}

    for index in range(len(arr)):
        if not hash.get(ar[index]):
            hash[ar[index]] = 1
        else:
            hash[ar[index]] = hash[ar[index]] + 1

    print(hash)


# Find the count of character using hashing

char_arr = ["a", "b", "c", "a", "b", "c", "d"]


def find_char_occ(char_arr):
    hash = {}
    for char in char_arr:
        # current_index = ord(char) - ord("a")
        if not hash.get(char):
            hash[char] = 1
        else:
            hash[char] = hash[char] + 1

    print(hash)


find_char_occ(char_arr)

# find_count(ar)
