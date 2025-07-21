def check_ferman(a,b,c,n):

    if n>2 and (a**n)+(b**n)==(c**n):
        print("Ferman was wrong!")
    else:
        print("Ferman was correct")

a = int(input("enter a"))
b = int(input("enter b"))
c = int(input("enter c"))
n = int(input("enter n"))
if n<=2:
    print("enter n greater than 2")
else:
    for i in range(1,a+1):
        for j in range(1,b+1):
            for k in range(1,c+1):
                check_ferman(i,j,k,n)
                print(i,j,k)

