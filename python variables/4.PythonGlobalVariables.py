#Create a variable outside of a function, and use it inside the function:

x = 10 # this is a global variable, because it is outside of a function, and can be used by anyone, both inside and outside of a function.

def sum():
    print (x + 5)

# sum()

#Create a variable inside a function, with the same name as the global variable:

x =15

def sum () :
    global x # this will tell Python that we want to use the global variable x, instead of creating a local variable with the same name.      
    print(x + 5)
    
    x=10 # this is a local variable, because it is inside a function, and can only be used inside that function.

#sum() # this will print 15, because the local variable x is used inside the function, and it has a value of 10, so 10 + 5 = 15.

#print(x) # this will print 10, because the global variable x is used outside the function, and it has a value of 10.


x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 
