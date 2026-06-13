#Python Logical Operators

x = 10 

print (x>5 and x<15)
print (x>5 or x<15)
print (not(x>5 and x<15)) #False because not operator changes the result of the expression to its opposite.

#this is my expremient with chaining comparison operators and logical operators:

print (not(5<x<15)) #not is applied to the chaining comparison operator, so it changes the result of the expression to its opposite.
