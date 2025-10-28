def print_n_times(n):
    if n==1:
        return n
    else:
        print("The number is ", n)
        print_n_times(n-1)

print_n_times(10)