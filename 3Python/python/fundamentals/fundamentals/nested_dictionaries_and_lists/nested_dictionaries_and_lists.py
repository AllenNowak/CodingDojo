# Update Values in Dictionaries and Lists
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)
# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# Change the value 20 in z to 30
z[0]['y'] = 30
print(z)


'''
# 2.
Iterate Through a List of Dictionaries
Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
the function loops through each dictionary in the list and prints each key and the 
associated value. For example, given the following list:
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel
'''

# Ugly - I'll learn a more pythonic way


def iterateDictionary(some_list):
    for entry in some_list:
        entryString = ''
        # Getting the length of the dictionary to help format the output string:
        # https://stackoverflow.com/questions/42193712/how-to-iterate-dict-with-enumerate-and-unpack-the-index-key-and-value-alon
        for i, (key, val) in enumerate(entry.items()):
            entryString += f'{key} - {val}{", " if (i < len(entry) - 1) else ""}'
        print(entryString)


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

print()
print('Testing Iterate Dictionary')
print('*'*20)
print()
iterateDictionary(students)

# 3. Get Values From a List of Dictionaries
'''
Get Values From a List of Dictionaries
Create a function iterateDictionary2(key_name, some_list) that, 
given a list of dictionaries and a key name, 
the function prints the value stored in that key for each dictionary. 
For example, iterateDictionary2('first_name', students) should output:
    Michael
    John
    Mark
    KB

And iterateDictionary2('last_name', students) should output:
    Jordan
    Rosales
    Guillen
    Tonel
'''


def iterateDictionary2(key_name, some_list):
    # print ([f'{i[key_name]}\n' for i in some_list]) doesn't print on separate lines
    for i in some_list:
        print(i[key_name])


iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


# 4. Iterate Through a Dictionary with List Values
'''
Iterate Through a Dictionary with List Values
Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
prints the name of each key along with the size of its list, and then 
prints the associated values within each key's list. For example:
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
# output:
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
'''


def printInfo(some_dict):
    for d in some_dict:
        print(f'{len(some_dict[d])} {d.upper()}')
        for detail in some_dict[d]:
            print(detail)
        print()


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
