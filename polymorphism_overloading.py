
#method overloading
class Calculation:
    def add(self, a: int, b: int, c: int=0):
        print(a + b + c)
cal =Calculation()
cal.add(1, 3)

#method overridding
class Employee:
    __amt = 20000
    def sal (self):
        return self.__amt * 12
class ContractEmployee(Employee):
    __hrpay = 1000
    __hrs=10
    def sal(self):
        return self.__hrpay * self.__hrs
emp = ContractEmployee()
print(emp.sal())

#constructor
class Employee:
    def fullName(self, fName, lName):
        print(fName + lName)
emp = Employee()
emp.fullName("suji", "swami")

#parameterless constuctor
class Employee:
    def __init__(self):
        pass
    def fullName(self, fName, lName):
        print(fName + lName)
emp = Employee()
emp.fullName("sujitha", "swami")

#parameterized constructor
class Employee:
    __fname: str = " "
    __lName: str =" "
    def __init__(self, fName, lName):
        self.__fname = fName
        self.__lName = lName
    def fullName(self):
        print(self.__fname + self.__lName)
emp = Employee("sujitha", "swami")
emp.fullName()
