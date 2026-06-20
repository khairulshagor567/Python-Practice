thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
# print(thisdict["colors"][0])

# thisDict = dict(name="khairul",age=35,country="Bangladesh")
# print(thisDict)

#Accessing Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
# print(x)
# print(thisdict.get('model'))
# print(thisdict.keys())

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change