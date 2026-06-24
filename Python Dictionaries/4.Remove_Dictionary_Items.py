#Removing Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "wheels":4,
  "color":"White",
  "seats":5
}

thisdict.pop("brand")
thisdict.popitem()
thisdict.clear()
del thisdict
print(thisdict)