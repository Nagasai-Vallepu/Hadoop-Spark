n=int(input("enter a number:"))
t=n
s=0
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
if s==t:
    print("it is a pallindrome")
else:
    print("it is not a pallindrome")
