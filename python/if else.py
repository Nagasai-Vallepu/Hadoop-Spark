a=int(input("enter 1st value:"))
b=int(input("enter 2nd value:"))
c=int(input("enter 3rd value:"))
if a==b and b==c:
    print("three values are equal")
else:
    if a>b and a>c:
        print("a is big")
    else:
        if b>c:
            print("b is big")
        else:
            print("c is big")