thisdict = {
  "brand": "Tata",
  "model": "Range Rover",
  "year": 2000
}
print(thisdict)

mydict = thisdict.copy()
print(mydict)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)

x = car.items()

print(x)

x = car.keys()

print(x)

car.pop("model")

print(car)

x = car.values()

car.clear()

print(car)

print(x)

x = car.setdefault("model", "Bronco")

print(x)

x = car.setdefault("model", "Bronco")

print(x)

car.update({"color": "White"})

print(car)