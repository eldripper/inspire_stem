# making and changing a list
# date : 28/02/2024
# name : elias

friends = ["jane","james","eli","grace","jef"]

for friend in friends :
    print(friend)

enemies = friends[:]# copy one list into another
print(enemies)

fruits = ["mango","melon","apple","banana","orange"]

# slice the list ;get a part of the list

print(fruits[0:3])

del fruits[0]
print(fruits)

squares = []# initializes an empty list

for x in range(0,11):
    squares.append(x**2)

print(squares)