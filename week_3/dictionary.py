# 



laptop = {"make":"lenovo","colour":"grey","weight":"1.6kg","date of birth":"2006"}


print(laptop["make"])
print(laptop["colour"])
print(laptop["date of birth"])

laptop["colour"] = "red"
laptop["date of birth"] = "2022"

print(laptop)

laptop["size"] = "1200mm x 600mm"
print(laptop)

del laptop["colour"]

print(laptop)

siz_laptop = laptop.copy()# copy dictionary

"""

for key, value in laptop.items():
    print(key)
    print("\n")
    print(value)

"""
