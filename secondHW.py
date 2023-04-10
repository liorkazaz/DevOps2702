# A
# def compare(x, y):
#    if x is str:
# B
for iteration in range(5):
    print(iteration)
# C
for season in range(1, 4):
    if season == 1:
        print("Summer")
    elif season == 2:
        print("Winter")
    elif season == 3:
        print("Fall")
    elif season == 4:
        print("Spring")
# D
# 1. 10
# 2. 10

# E
my_dict = {
    "age": 36,
    "last_name": 'K',
    "shekel_dollar": 3.59,
    "abroad": True,
    "apartment": 4
}
print(my_dict)
print(my_dict["age"] + my_dict["shekel_dollar"])

# F
phone_entered = input("Please enter phone number: ")
print("phone number " + phone_entered)

# G
# 1.
def printHello():
    print("hello")
# 2.
def calculate():
    print(5 + 3.2)

# H
# 1.
def printName(name):
    print(name)
# 2.
def dividebytwo(number):
    if number is int or number is float:
        print(number / 2)
# H
# 1.
def myAdd(number1, number2):
    if number1 is int or number1 is float and number2 is int or number2 is float:
        return number1 + number2
# 2.
def addSpace(string1, string2):
    if string1 is str and string2 is str:
        return string1 + " " + string2
# K
for row in range(1, 6):
    for brick in range(row):
        print( "*", end='')
    print()

# L
max = 7
for line in range(max):
    print(line)




