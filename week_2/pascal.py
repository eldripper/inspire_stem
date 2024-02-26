# pascal's triangle
# date : 22/02/2024
# name : elias

from math import factorial

rows = int(input("enter the number of rows : "))
for n in range(rows):
    for space in range(1, rows - n):
        print(end = " ")

    for r in range(n+1):
        ncr = factorial(n)//(factorial(r) * factorial(n - r))
        print(ncr, end = "  ")

    print(" ")