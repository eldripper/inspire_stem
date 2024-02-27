input("employee full name :")
input("age of employee :")
salary = float(input("salary :"))


if salary < 100000 :
    bonus = salary * 30/100
    total_salary = salary + bonus
    print(total_salary)


elif salary > 100000 and salary < 150000 :
    bonus = salary * 15/100
    total_salary = salary + bonus
    print(total_salary)


else :
    salary > 150000 
    bonus = salary * 5/100
    total_salary = salary + bonus
    print(total_salary)
    