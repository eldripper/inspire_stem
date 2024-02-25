# strings in python
# date :22/02/2024
# name : eli

city = "nairobi"
print(city[0])# will print n
print(city[1])# will print a
print(city[2])
print(city[3])


print(city[-3])
print(city[-2])# will start from behind
print(city[-1])

# how to convert to uppercase
print(city)
print("\n\n")# prints a new line
print(city.upper())

name = "ELIAS GITHINJI"
print(name)
print(name.lower())# converts to lowercase


town = "   Naivasha"
print(town)
print("\t") # new tab
print(town.strip())

# add strings

f_name = "elias"
s_name = "githinji"

full_name = f_name + s_name
print(full_name)

# replacing a character

fruit = "orangeoooo"
print(fruit.replace('o','y'))

subject = "physical: sciences: biology"
print(subject.split(":"))

age = 39
height = 5.7 

print("i am {0} yrs old and {1} meters tall".format (age,height))