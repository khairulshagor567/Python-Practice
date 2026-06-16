#Python Update Tuples
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

#Add Items

tuple1 = ("apple","orange","cherry")
tuple2 = list(tuple1)
tuple2.append("mango")
tuple2.insert((len(tuple2)),"Khejur")
# print(tuple(tuple2))

tuple3 = ("Jackfruit","Guava")
tuple4 = list(tuple3)
tuple2.extend(tuple4)
print(tuple2)

#2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

thistuple = ("apple", "banana", "cherry")
y =("Orange",)
thistuple +=y
# print(thistuple)
