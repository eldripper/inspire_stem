# functions are a block of code running together as a unit



# we first initialize a function then call the function - using a keyword called (def)

# define the function
def print_name():
    print ("my name is elias githinji")


# calling the function
print_name()
print_name()
print_name()
print_name()


def print_details(name, age, ID, gender):
    print("i am {0}, {1} years old. my ID number is {2} and my gender is {3}.".format(name, age, ID, gender))


print_details("elias", "18", "22704826", "male")
print_details("grace", "13", "3933", "female")



def sum_nums(x,y):
    return x + y


z = sum_nums(10,20)
print(z)


def prod_nums(x,y):
    return x * y

print(prod_nums(5,86))

def print_odds(fnumber, lnumber):
    for i in range(fnumber, lnumber):
        print(i %2)

print_odds(0, 20)


