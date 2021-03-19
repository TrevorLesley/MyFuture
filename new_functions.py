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
def age():
    age = input("Enter your age:")
    int_age = int(age)
    if int_age < 21:
        print("Youngin")
    else:
        print("Ancient")
 
################

#Optional parameters

def f(x=2):
    return (x**x)

###############
# division 
def division():
    a = input("Type a number:")
    b = input("Type another:")
    a = int(a)
    b = int(b)
    return (a/b)

###############

# Exception Handling
def exception():
    a = input("Type a number:")
    b = input("Type another:")
    a = int(a)
    b = int(b)
    # print(a," A")
    # print(b, "B")
    # print (a/b, " A/B")
    try:
        print(a / b)
    except ZeroDivisionError:
        print("b cannot be zero.")

# More Exception Handling
def exception2():
    try:
        a = input("Type a number:")
        b = input("Type another:")
        a = int(a)
        b = int(b)
        print((a/b))
    except (ZeroDivisionError, ValueError, NameError):
        print("Invalid input.")

#########################

""" Freestyle Programs """

def energy():
    energy = input("On a scale of 1-100, how are you feeling?")
    int_energy = int(energy)
    if int_energy < 10:
        print("Not so good, huh?")
    else:
        print("You're chilling.")


def batterylife():
    batterylife = input("What's your charge?")
    int_batterylife = int(batterylife)
    if (int_batterylife<=10):
        print("Please plug your device in.")
    elif (int_batterylife>=11) and (int_batterylife<=50):
        print("Needs charging soon.")
    elif (int_batterylife>89):
        print("Battery charged.")
    else:
        print("Healthy charge.")
    

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

# age()

#print(f())
#print(f(4))

#division
#division()

#exception()
#exception2()

#energy()
batterylife()