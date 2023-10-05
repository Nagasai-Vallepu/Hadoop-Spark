class Student:
    def getinfo(self):
        self.regno = int(input("Enter Regno : "))
        self.sname = input("Enter name : ")

    def getmarks(self):
        self.maths = int(input("Enter maths marks : "))
        self.computer = int(input("Enter computers marks : "))
        self.stats = int(input("Enter statistics marks : "))

    def display(self):
        self.total = self.maths + self.stats + self.computer
        print("Regno", self.regno)
        print("Sname", self.sname)
        print("Maths =", self.maths, "computers=", self.computer, "stats =", self.stats)
        print("Total =", self.total)

s1 = Student()
s1.getinfo()
s1.getmarks()
s1.display()