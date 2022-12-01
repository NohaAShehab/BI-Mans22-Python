# emp={
#     "name":"Ahmed",
#     "email": "ahmed@gmail.com",
#     "salary": 10000
# }
# emp2 = {
#     "empname":"meran",
#     "email":"meran@gmail.com",
#     "empsalary":10000
# }
#
# emp3 = {
#     "empname":"meran",
#     "email":"meran@gmail.com",
#     "empsalary":10000,
#     "branch":'Mansoura'
# }

# "1- define a class  ---> user defined class"
# class Employee:
#     pass
#
# e = Employee()
############################
"1- define a class  ---> user defined class"
# class Employee:
#     # this function is being called every you create new object
#     def __init__(self):
#         print(f"self = {self}")
#         self.name = 'Ahmed'
#         self.email= 'ahmed@gmail.com'
#         self.salary= 10000
#         print("---- new employee object is being created ")
#
# e = Employee()
# print(e)
# print(f"Employeename = {e.name}")
# print(f"email = {e.email}")
# print(f"salary = {e.salary}")
# e.name = 'Ali'
# e.country = 'Cairo'
# # # e2 = Employee()
# # # print(e2)

########################3



# class Employee:
#     __slots__ = ["name", "email", "salary"]
#     # this function is being called every you create new object
#     def __init__(self):
#         print(f"self = {self}")
#         self.name = 'Ahmed'
#         self.email= 'ahmed@gmail.com'
#         self.salary= 10000
#         print("---- new employee object is being created ")
#
# e = Employee()
# print(e)
# print(f"Employeename = {e.name}")
# print(f"email = {e.email}")
# print(f"salary = {e.salary}")
# e.name = 'Ali'
# e.country = 'Cairo'
# # e2 = Employee()
# # print(e2)
########################################################
# class Employee:
#     # this function is being called every you create new object
#     def __init__(self,name, email, salary):
#         print(f"self = {self}")
#         self.name = name
#         self.email= email
#         self.salary= salary
#         print("---- new employee object is being created ")
#
# e = Employee("Ahmed", "ahmed@gmail.com", 10000)
# print(e)
# e2 = Employee("Ali", "Ali@gmail.com", 20000)
##############################################33
""" constructor with default arguments """
#
# class Employee:
#     # this function is being called every you create new object
#     def __init__(self,name="", email="", salary=0):
#         print(f"self = {self}")
#         # name , email , salary ---> instance variables
#         self.name = name
#         self.email= email
#         self.salary= salary
#         print("---- new employee object is being created ")
#
# e = Employee("Ahmed", "ahmed@gmail.com", 10000)
# print(e)
# # e2 = Employee()
# ###########################################
#
#
# class Employee:
#     # this function is being called every you create new object
#     def __init__(self,name="", email="", salary=0):
#         # name , email , salary ---> instance variables
#         self.name = name
#         self.email= email
#         self.salary= salary
#
#     # instance method ---> we use to apply operation on the instnace
#     def printEmpInfo(self):  # self ---> refer to the address of the current object
#         print("----displaying the Employee Information..... ")
#         print(f"Employee name={self.name}, employee email= {self.email}, employee salary={self.salary}")
#
#     def greetEmp(self, message):
#         print(f"{message}, {self.name}")
#         return True
#
# e = Employee("Ahmed", "ahmed@gmail.com", 10000)
# print(e.email)
# e.printEmpInfo()
# e.greetEmp("Nice to meet you ")
# e2 = Employee()
# print(e2.email)
# e2.email = 'update@gmail.com'

# class Car:
#     def __init__(self, color, velocity):
#         self.color =color
#         self.velocity = velocity
#
#     def increasevelocity(self):
#         self.velocity +=10
#
# c = Car("Red", 40)
# c.increasevelocity()


########
# class Human:
#     count = 0  # class variable
#     country = "Egypt"
#     def __init__(self,name,address):
#         self.name = name
#         self.address = address
#
#         Human.count +=1
#
#
#     def speak(self):
#         print(self)
#         print(f"My name is {self.name}, I lives at {self.address}")
#
#     ###########333 class method ###############
#     @classmethod
#     def get_human_count(cls):
#         print(cls)
#         print( cls.count)
#
#     ### class method is used as object factory
#     @classmethod
#     def createDefaultObj(cls):
#         return  cls("default", "default")
#
# # h = Human("noha", "Mansoura")
# # h.speak()
# # print(Human.count)
# # Human.country = 'Saudi Arabia'
# # h2 = Human("Mostafa", "Mansoura")
# # print(Human.count)
#
# h4 = Human.createDefaultObj()
#
# Human.get_human_count()
#
#
#
#
#
#######################
# class MyComplex:
#     def __init__(self, real, img):
#         self.real =real
#         self.img = img
#
#
#     @classmethod
#     def add_complex(cls, c1, c2):
#         real = c1.real +c2.real
#         img= c1.img + c2.img
#         c3= cls(real, img)
#         return c3
#
#
# c1 = MyComplex(4,5)
# c2 = MyComplex(10, 20)
#
# c3 = MyComplex.add_complex(c1, c2)


##################################
# static method

class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.salary= salary

    @staticmethod
    def calnetsal(sal):
        return sal * .8

e = Employee("Ahmed",10000)
print(Employee.calnetsal(100000000))
print(Employee.calnetsal(e.salary))
# def calnetsal(sal):
#     return sal*.8

# print(calnetsal(e.salary))
# print(calnetsal(100000))











































