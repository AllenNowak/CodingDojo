num1 = 42                           # variable declaration, primitive, number 
num2 = 2.3                          # variable declaration, primitive, number 
boolean = True                      # variable declaration, primitive, boolean
string = 'Hello World'              # variable declaration, primitive, string 

# variable declaration, composite. list, initialization
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

# variable declaration, composite. dictionary, initialization
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

# variable declaration, composite. tuple, initialization
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit))                   # log statement, type check
print(pizza_toppings[1])             # log statement, access value of list
pizza_toppings.append('Mushrooms')   # list add value
print(person['name'])                # log statement, access value of dictionary
person['name'] = 'George'            # list change value
person['eye_color'] = 'blue'         # list add value
print(fruit[2])                      # log statement, access value of tuple

if num1 > 45:                        # conditional if, numeric primitive data type & numeric literal
    print("It's greater")            # log statement
else:                                # conditional else
    print("It's lower")              # log statement

if len(string) < 5:                  # conditional length check of primitive string data type, numeric literal
    print("It's a short word!")      # log statement
elif len(string) > 15:               # conditional else if, length check of primitive string data type, numeric literal
    print("It's a long word!")       # log statement
else:                                # conditional else
    print("Just right!")             # log statement

for x in range(5):                   # for loop start 0, stop 4, increment 1, sequence
    print(x)                         # log statement
for x in range(2,5):                 # for loop start 2, stop 4, increment 1, sequence
    print(x)                         # log statement
for x in range(2,10,3):              # for loop start 2, stop 9, increment 3, sequence
    print(x)                         # log statement
x = 0                                # numeric variable assignment
while(x < 5):                        # while loop start 0, stop 4
    print(x)                         # log statement
    x += 1                           # while loop increment 1, 3, 7, while loop stop condition

pizza_toppings.pop()                 # composite, list, delete value
pizza_toppings.pop(1)                # composite, list, delete value

print(person)                        # log statement
person.pop('eye_color')              # list delete value
print(person)                        # log statement

for topping in pizza_toppings:       # variable declaration string, composite list access value
    if topping == 'Pepperoni':       # conditional if
        continue                     # for loop continue
    print('After 1st if statement')  # log statement
    if topping == 'Olives':          # conditional if
        break                        # for loop break

def print_hello_ten_times():         # function, no parameters
    for num in range(10):            # for loop start 0, stop 9, incremente 1
        print('Hello')               # log statement

print_hello_ten_times()              # function invocation w no arguments

def print_hello_x_times(x):          # function, parameter = x
    for num in range(x):             # variable declaration of numeric primitive, function call w/ argument x
        print('Hello')               # log statement

print_hello_x_times(4)               # function, argument 4

def print_hello_x_or_ten_times(x = 10):   # function, variable declaration & assignment, argument = x defaulting to 10 if not passed by caller
    for num in range(x):                  # variable declaration, data type numeric primitive, function call with argument x
        print('Hello')                    # log statement

print_hello_x_or_ten_times()              # function call with no argument
print_hello_x_or_ten_times(4)             # function call with argument 4


"""                                 # multi line comment
Bonus section                       # multi line comment
"""                                 # multi line comment

# print(num3)                       # Single line comment, NameError: name <variable name> is not defined
# num3 = 72                         # Single line comment, variable declaration, assignment of numeric primitive
# fruit[0] = 'cranberry'            # Single line comment, TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team'])    # Single line comment, KeyError: 'favorite_team'
# print(pizza_toppings[7])          # Single line comment, IndexError: list index out of range
#   print(boolean)                  # Single line comment, IndentationError: unexpected indent
# fruit.pop(1)                      # Single line comment, AttributeError: 'tuple' object has no attribute 'append'
# fruit.append('raspberry')         # Single line comment, AttributeError: 'tuple' object has no attribute 'pop'
