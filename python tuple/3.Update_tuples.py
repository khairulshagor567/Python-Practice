#Python Update Tuples
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
tuple1 = ("apple","orange","cherry")
tuple2 = list(tuple1)
tuple2.append("mango")
tuple2.insert((len(tuple2)),"Khejur")
print(tuple2)