some_nums = [44,56,2,3,12,19,6]
print("Get started by writing your own code!")

# Some optional challenges to assess and refine your understanding:

# Print the length of the list.
print(len(some_nums))

# Use antoher python built-in function and print the result.
copy = some_nums[:]
some_nums.reverse()
revd = some_nums[:]
print('copy:', copy)
print('revd:', revd)

# Remove an item from the list. Remember to verify that it was removed.
ppd = some_nums.pop()
print('ppd:', ppd)

# Utilize a method from the documentation and print the result.

matrix = [
    [11, 12, 13, 14],
    [21, 22, 23, 24],
    [31, 32, 33, 34]
]
transposition = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print('matrix', matrix)
print('transposition', transposition)
