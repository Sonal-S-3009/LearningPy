'''import math
def hypotenuse(x,y):
    return math.sqrt((x**2)+(y**2))

print(hypotenuse(3,4))'''

#boolean function
'''def is_between(x,y,z):
    return x<=y<=z

print(is_between(2,3,4))'''

'''def palindrom(s1):
    return s1==s1[::-1]

print(palindrom('asdfbbfdsa'))'''

def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

print(gcd(10,5))