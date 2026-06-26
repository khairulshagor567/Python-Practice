#Nested Dictionaries

myfamilys = {
    "1stChild":{
        "name":"Sawban Bin Khiarul",
        "age": 4.5,
        "gender":"male",
        "year": 2021
    },
    "2ndChild":{
        "name":"Arwa Binte Khairul",
        "age": 1.6,
        "year": 2025
    }
}
# for x in myfamilys:
#      print(myfamilys[x]['name'])


childOne = {
    "name" : "Sawban Bin Khairul",
    "age"  : 4.6,
    "year" : 2021
}

childTwo = {
    "name" : "Arwa Binte Khairul",
    "age"  : 1.6,
    "year" : 2025
}

myFamily ={
    "child1" : childOne,
    "child2" : childTwo,
}

print(myFamily)
    