n=int(input("enter a number:"))
t=n
s=0
while n>0:
    r=n%10
    s=s+r**3
    n=n//10
if s==t:
    print("It is a armstrong")
else:
    print("It is not a armstrong")