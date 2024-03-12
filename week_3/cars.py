# this is a class that describes cars

class car:
    def __init__(self ,model, make, year, fuel_capacity, colour, horse_power):
        self.model = model
        self.make = make
        self.year = year
        self.fuel_capacity = fuel_capacity
        self.colour = colour
        self.horse_power = horse_power

    def print_make(self, make):
        print("the car is of {0} make".format(self.make))

    def set_make(self, make):
            self.make = make

    def get_make(self):
            return self.make


my_car = car("Impalla", "chevrolet", "1969", "2500 cc", "lilac", "2500")

friends_car = car("note", "nissan", "1969", "2500 cc", "lilac", "780")

my_car.print_make("chevrolet")


my_car.set_make("ford")
friends_car.set_make("toyota")

print(my_car.get_make())
print(friends_car.get_make())