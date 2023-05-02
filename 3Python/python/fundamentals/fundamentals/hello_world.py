# 1. TASK: print "Hello World"
print('Hello World')
# 2. print "Hello Noelle!" with the name in a variable
name = "Allen"
# 2a use the variable to print the string "Hello {{your name}}! "
print('Hello', name)  # with a comma
print('Hello ' + name)  # with a + #2b
# 3. print "Hello 42!" with the number in a variable
name = 42
print('Hello', str(name), '!')  # with a comma
# with a +	-- this one should give us an error! # unless I use: 'Hello ' + str(name)...
print('Hello ' + str(name) + '!')
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "cheeseburgers"
fave_food2 = "deep dish pizza"
print("I love to eat {} and {}.".format(
    fave_food1, fave_food2))  # with .format() #4a
print(f"I love to eat {fave_food1} and {fave_food2}.")  # with an f string #4b

twain_essay = 'on the decay of the art of lying is an essay by mark twain'

print()
index_of_by = twain_essay.index('by')
index_of_author = index_of_by + 3
print(twain_essay[:index_of_by].title())
# print('by'.center(len(twain_essay)))
print('by'.rjust(index_of_author - (len(twain_essay) - index_of_by)))
print(twain_essay[index_of_author:].upper().rjust(index_of_by - 1))
