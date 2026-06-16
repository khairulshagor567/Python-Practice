#Python - Unpack Tuples:

fruits = ("apple", "banana", "cherry")
(green,yellow,red)=fruits
# print(green+"=="+yellow+"=="+red)

#Using Asterisk* for tuple and list items:

fruits = ["apple", "banana", "cherry", "strawberry", "raspberry"]
[fruit1,fruit2,*fruit3,fruit4] = fruits
print(fruit3)
                      