def f(x):
    return (x * 2)
    
result = f(2)
print(result, " result problem 1")


################# 

#These return statements need parentheses

def z(v):
    return (v+1)

y = z(4)
print(y)

if y == 5:
    print("y is 5 result problem 2")
else:
    print("y is not 5 result problem 2")


#################

def f():
    return (1+1)


result = f()
print(result)

#################

def f(x, y, z):
    return (x+y+z)


result = f(1, 2, 3)
print(result, " result problem 3")

##########################

age = input("Enter your age:")
int_age = int(age)
if int_age < 21:
    print("Youngin")
else:
    print("Ancient")
 