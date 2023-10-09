# input start and end value display armstrong range
st = int(input("enter start number:"))
e = int(input("enter end number:"))
while st <= e:
    t = st
    s = 0
    while t > 0:
        r = t % 10
        s = s + r ** 3
        t = t // 10
    if st == s:
        print(st, "it is a armstrong")
    st = st + 1


