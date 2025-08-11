"""
Print below pattern :

*
* *
* * *
* * * *
* * * * *
* * * * * *

"""

no_of_lines = 6

for i in range(0, no_of_lines):
    for j in range(0, i + 1):
        print("*", end="")
    print()
