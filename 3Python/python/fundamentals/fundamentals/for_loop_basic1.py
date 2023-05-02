import functools

# 1. Basic - Print all integers from 0 to 150.
for x in range(0, 150):
    print(x)

print()
# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for x in range(5, 1000, 5):
    print(x)

print()
# 3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range(1, 100):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

print()
# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
max_value = 500000
sum = 0
nums = range(max_value)
for num in nums:
    if num % 2 == 1:
        sum += num
sum = functools.reduce(lambda a, b: a+b if a % 2 == 1 else a+0, nums)
print(f'for loop sum using mod 2 == 1 = {sum:,}')

sum = 0
for i in range(1, max_value, 2):
    sum += i
print('sum over range with step == 2 = ', end='')
print(f'{sum:,}')
'''
in the range 0..500,000
1 + 499,999 == 500k
3 + 499,997 == 500k
5 + 499,995 == 500k, etc
there are 500k * 1/2 such pairs from 0..500k, 1/2 of those are odd pairs
=> 500k * (1/4 of 500k steps) == the sum of odd pairs
'''
product = int(max_value * (0.25 * max_value))
print(f'sum of odds is the product of (odd pairs * max value) =  {product:,}')


print()
# 5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for i in range(2018, 0, -4):
    print(i)


print()
# 6. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum+1):
    if (i % mult == 0):
        print(i)
