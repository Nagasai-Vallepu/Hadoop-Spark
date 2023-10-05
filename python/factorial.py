n=int(input("enter a number :"))
fact=1
for i in range(1,n+1):
    if n>=1:
        fact=fact*i
print("Factorial of a %d is :" %i,fact)