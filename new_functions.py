" Defining Functions"

def a(x):
    return (x * 2)
    
################# 
#These return statements need parentheses

def z(v):
    return (v+1)

#################
def h():
    return (1+1)


#################
def g(x, y, z):
    return (x+y+z)


##########################

# age = input("Enter your age:")
# int_age = int(age)
# if int_age < 21:
#     print("Youngin")
# else:
#     print("Ancient")
 
################

#Optional parameters

def f(x=2):
    return (x**x)

###############
# division 
a = input("Type a number:")
b = input("Type another:")
a = int(a)
b = int(b)


""" Function Calls """
# result = a(2)
# print(result, " result problem 1")


# result = g(1, 2, 3)
# print(result, " result problem 3")


# result = h()
# print(result, " Result H")


# y = z(4)
# print(y, " Result Y")
# if y == 5:
#     print("y is 5 result problem 2")
# else:
#     print("y is not 5 result problem 2")


#print(f())
#print(f(4))

#division
print(a / b)