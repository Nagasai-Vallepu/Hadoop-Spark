class Demo:
    def __init__(self):
        print("From constructor of class Demo")
        self.a = int(input("Enter value : "))
        self.x = None

    def show(self):
        self.x = "Hyderabad"
        print("From show method of class demo", self.x)
        print("From show method of class demo",self.a)

d1 = Demo()
d2 = Demo()
print("value from object1", d1.a)
print("value from object2", d2.a)
d1.show()
d2.show()