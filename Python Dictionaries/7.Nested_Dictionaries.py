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
for x in myfamilys:
     print(myfamilys['1stChild']['name'])
    