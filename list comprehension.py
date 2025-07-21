import math
import time
from logging import raiseExceptions

from Module import factorial, fibonaci

'''# For loop
start = time.time()
result = []
for i in range(10_000_000):
    result.append(i * 2)
print("For loop:", time.time() - start)

# List comprehension
start = time.time()
result = [i * 2 for i in range(10_000_000)]
print("List comp:", time.time() - start)
'''


'''import time

data = list(range(1_000_000))

# Manual tracking
start = time.time()
i = 0
for val in data:
    i += 1
end = time.time()
print("Manual:", end - start)

# Using enumerate
start = time.time()
for i, val in enumerate(data):
    pass
end = time.time()
print("Enumerate:", end - start)'''

'''lst = [x**2 for x in range(1,21) if x%2==0]
print(lst)'''

'''nums = ['one','two','three','four','five']
d = {x:i for x, i in zip(range(1,6),nums)}
print(d.items())'''

'''s = 'ajbaisduusnlsocgus'
v = 'aeiou'
unique = {i for i in s if i in v}
print(unique)'''

#generator

'''def fib(n):
    a,b =0,1
    for _ in range(n):
        yield a
        a,b = b ,a+b

x = fib(10)
print(list(x))
for i in x:
    print(i)
'''

'''mat = [[1 if i==j else 0 for j in range(3)]for i in range(3) ]
for row in mat:
    print(row)'''

'''text = 'a big cow as eating the grass, while a big monkey was one the tree, looking surprised'
words = text.split()
count = {word: words.count(word) for word in set(words) }
print(count)'''

#flatten a 2d list in 1d
'''x = [[1,2],[3,4],[5,6]]
flat = [j for i in x for j in i]
print(flat)'''

'''n =10
divisor = {i for i in range(1,n) if n%i ==0 }
print(divisor)'''
import math
'''nums = [1,2,3,4,5,6,7,8,9]
non_prime = [i for i in nums for j in range(2,i) if i%j ==0]
print(non_prime)'''

'''l1 = [1,2,3,5,6,7,8]
l2 = [1,4,7,8,4,7,9]
pair = [(i,j) for i in set(l1) for j in set(l2) if i!=j]
print(pair)'''

#Write a generator expression to process a large file line by line, yielding lines containing a specific keyword.


'''keyword = 'ERROR'

matching_lines = (line for line in open('sample_text.txt') if keyword in line)
for line in matching_lines:
    print(line)'''

'''def read_file(file):
    try:
        with open(file) as f:
            data = f.readlines()
            return data
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denied")
    finally:
        print("Operation executed")

name = 'sample_text2.txt'
print(read_file(name))'''

'''def dev(a,b):
    try:
        c = a/b
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except TypeError:
        print("TypeError")

print(dev(2,0))'''

# Custom exception class
'''class ValidationError(Exception):
    def __init__(self, data):
        self.data = data
        super().__init__(f"Invalid value: {data}")

# Function using the custom exception
def func(a):
    try:
        if a < 0:
            raise ValidationError(a)
        a += a
        return a
    except ValidationError as e:
        print("Value less than zero / Not valid:", e)

# Test
print(func(-2))
print(func(5))
'''

import Module
print(factorial(5))
print(fibonaci(5))
