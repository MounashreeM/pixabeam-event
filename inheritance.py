'''lass Programmer:
    company="mnc"
    def func(self):
        print(f"name of compant{self.company}")
class testor(Programmer):
    name="employee n"         
    def func(self):
        print(f"name of compant{self.company}of employe{self.name}")  

a=Programmer()
b=testor()
b.func()'''

class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    def display(self):
        print("Child class")

c = Child()
c.show()
c.display()
