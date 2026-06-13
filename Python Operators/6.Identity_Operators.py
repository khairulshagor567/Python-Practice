#Python Identity Operators

#The is operator returns True if both variables point to the same object:
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) #True because z is pointing to the same object as x.
print(x is y) #False because x and y are two different locations in memory.
print(x == y) #True because x and y are equal, but not the same object.