import math

print("""
1.add
2.sub
3.multipli
4.division
5.exponent
""")
operation = int(input("please choose operation you want to do:"))
num1 = int(input("please enter the first value:"))
num2 = int(input("please enter the second value:"))
if operation == 1:
    print("result=", num1 + num2)
elif operation == 2:
    print("result=", num1 - num2)
elif operation == 3:
    print("result=", num1 * num2)
elif operation == 4:
    print("result=", num1 / num2)
elif operation == 5:
    print("result=", num1 ** num2)

else:
    print("invalid operation")














