def fibonaci(data):
    a,b = 0,1
    fib = [a]
    for _ in range(data):
        fib.append(a+b)
        a,b = b,a+b
    return fib

def factorial(data):
    fact = 1
    while data>0:
        fact *=data
        data -=1
    return fact


