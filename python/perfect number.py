n=int(input("enter a number:"))
i=1
sum=0
while i<n:
    if n%i==0:
        sum=sum+i
    i=i+1
if n==sum:
    print(n,"It is a perfect number")
else:
    print(n,"It is not a perfect number")
