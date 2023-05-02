# 1. Countdown using list comprehension
def countdown(n):
    return [x for x in range(n, -1, -1)]


print(countdown(5))

# 2. Print and return


def print_and_return(two_el_list):
    print('Printed value = ', two_el_list[0])
    return two_el_list[1]


x = print_and_return([1, 2])
print(f'returned value = {x}')

# 3. First Plus Length


def first_plus_length(stuff):
    return stuff[0] + len(stuff)


print(first_plus_length([1, 2, 3, 4, 5]))

# 4. values_greater_than_second
'''
- Write a function that accepts a list and creates a new list 
containing only the values from the original list that are greater than its 2nd value. 
Print how many values this is and then return the new list. If the list has less than 2 elements, 
have the function return False
Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
Example: values_greater_than_second([3]) should return False
'''


def values_greater_than_second(orig_list):
    if len(orig_list) < 2:
        return False

    second = orig_list[1]
    filtered_list = [x for x in orig_list if x > second]
    print(len(filtered_list))
    return filtered_list


print(values_greater_than_second([5, 2, 3, 2, 1, 4]))
print(values_greater_than_second([3]))

# 5. this length that value
''' 
This Length, That Value - Write a function that accepts two integers as parameters: size and value. 
The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
Example: length_and_value(4,7) should return [7,7,7,7]
Example: length_and_value(6,2) should return [2,2,2,2,2,2]
'''


def length_and_value(size, value):
    return [value for i in range(size)]


print(length_and_value(4, 7))
print(length_and_value(6, 2))
