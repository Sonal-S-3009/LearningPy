'''lst = [1,2,3,4,5,5,6,7,7,5,3,6]

def first_duplicate(l):
    seen = set()
    for item in lst:
        if item in seen:
            return item
        seen.add(item)

print(first_duplicate(lst))'''

'''def factorial(n):
    fact =1
    while n>0:
        fact *=n
        n -=1
    return fact

n = 5
print(factorial(n))'''

'''nest = [[1,2],[3,4],[5,6]]
flat = []
for i in nest:
    for j in i:
        flat.append(j)
print(flat)'''



'''from functools import lru_cache
class iterator:
    def __init__(self,n):
        self.n = n
        self.zero = 0
        self.one =1
    @lru_cache(maxsize=None)
    def fib(self,f):
        if f ==0:
            return 0
        elif f ==1:
            return 1
        else:
            return self.fib(f-1)+ self.fib(f-2)

    def fibonaci(self):
        return [self.fib(i) for i in range(1,self.n +1)]

obj = iterator(10)
print(obj.fibonaci())'''

'''def reverse(s):
    n = len(s)
    revrs = ""
    while n>=1:
        revrs = revrs + s[n-1]
        n -=1
    return revrs
print(reverse("hsudhwncjs"))'''


'''n = 50  # Replace with any desired upper limit

primes = [x for x in range(2, n+1) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
print(primes)'''

gen = (x  for x in range(50) if x%2 ==0)
for i in gen:
    print(i)
print(gen)


