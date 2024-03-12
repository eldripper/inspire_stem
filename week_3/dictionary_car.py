# about my favorite car
# date : 28/02/2024
# name : elias githinji


car = {"make":"bugatti chiron","colour":"black","horsepower":"1,500","date of birth":"2006"}


print(car["make"])
print(car["horsepower"])
print(car["date of birth"])

car["horsepower"] = "2,500"
car["date of birth"] = "2022"

print(car)


bro_car = car.copy()# copy dictionary

print(bro_car)

for key, value in car.items():
    print(key)
    print("\t")
    print(value)


