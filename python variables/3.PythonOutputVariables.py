
#In the print() function, you output multiple variables, separated by a comma:

x = "Python"
y = "is"
z = "awesome."
# print(x, y, z)

#You can also use the + operator to output multiple variables:

x = "Python"
y = "is"
z = "awesome."
#print(x + " "+ y + " "+ z)

#For numbers, the + character works as a mathematical operator:
x = 5
y = 10
# print(x + y)

#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
x = 5
y = "khairul"

#print(x + y)  #this will give an error because you cannot combine a string and a number with the + operator.
#print(x,y) this will work because the print() function can output multiple variables, separated by a comma.
# print(str(x) +" "+ y) #this will work because the str() function converts the number into a string, so you can combine it with the + operator.