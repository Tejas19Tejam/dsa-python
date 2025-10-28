"""

* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *

"""

for i in range(0, 5):  # rows
    for j in range(0, (5 + i - 5)):  # spaces
        print(" ", end=" ")
    for k in range(0, (2 * 5 - (2 * i + 1))):  # stars
        print("*", end=" ")
    print()
