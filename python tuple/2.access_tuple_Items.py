#Access Tuple Items

thisTuple = ("apple","banana","orange")
#print(thisTuple[0])

#Negative Indexing

tuple_fruits = ("Mango","Apple","Orange")
#print(tuple_fruits[-2]) 

#Range of Indexes:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:6])
print(thistuple[:4]) # data is available from 0 to 3
print(thistuple[2:]) # data is available from 2 to last items still.

#Range of Negative Indexes

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])

#Check if Item Exists

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")