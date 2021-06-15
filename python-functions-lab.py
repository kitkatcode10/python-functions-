# 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(n):
    sum = 0 
    for n in range(1, n + 1):
        sum += n
    return sum 

print(sum_to(6))

# 2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(nums):
    return max(nums)

print([largest([1, 2, 3, 4, 0])])

# 3. Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

# def occurances(string1, string2):
#     if string2 in string1
#     return occurances.count(string1, string2)

# print(occurances('fleep floop', 'ee'))
# this was my first attempt

def occurances(string1, string2):
    return string1.count(string2)

print(occurances('fleep floop', 'ee'))


# 4. Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.
(HINT: Review your notes on *args).

def product(*args):
    product = 1
    for arg in args:
        product *= arg 
    return product

print(product(-1,4)) 