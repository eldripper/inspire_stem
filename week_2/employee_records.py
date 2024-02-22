# this is a program that allows employees to enter their full names and other details
# date : 21/02/2024
# name : elias githinji

input("employee full name :")
input("age of employee :")
salary = float(input("salary :"))
bonuses = float(input("bonus :"))

inc = 130/100

salary_after_inc = inc*salary

bonus_after_inc = bonuses-5000

print("salary after increment :",salary_after_inc)

print("bonus after increment :",bonus_after_inc)

