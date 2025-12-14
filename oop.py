class Employee:
    

    def __init__(self,company,name,salary):
        self.company=company
        self.name=name
        self.salary=salary
        
    @staticmethod
    def func():
        print("hi good company")

comp=Employee("mnc","mouna",36678)
comp.func()
nim=Employee("hcl","nish",234688)

nim.salary=4666768
print(comp.company)
print(nim.salary)