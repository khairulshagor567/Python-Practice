#Python List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newList = []

# for x in fruits:
#     newList.append(x.upper())

# print(newList)
# newList = []
# for x in fruits:
#     if "a" in x:
#         newList.append(x)

# print(newList)
#[expression for item in iterable if condition == True]
#[print(x) for x in fruits if "a" in x]

#[print(x) for x in fruits if "a" in x]

# newList = [x for x in fruits if "a" in x]
# print(newList)

# newList = [x for x in fruits if x!="apple"]
# print(newList)

# newList = [x for x in fruits]
# print(newList)

newlistNumbers = [x for x in range(10)]
print(newlistNumbers)

newList = [x if x!="banana" else "orange" for x in fruits]
print(newList)



