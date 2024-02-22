# this is a program to calculate hire purchase price
# date : 21/02/2024
# name : elias githinji


d = int(input("enter the deposit :"))
t = int(input("enter the time in months :"))
m = int(input("enter the value of each installment :"))

hpp = d + (t * m)
print("the hire purchase prise is ",hpp)