n=int(input("enter a number:"))
i=2
while i<n:
    if n%i==0:
        print("It is not a prime number")
        break
    i=i+1
if i==n:
    print("It is a prime number")