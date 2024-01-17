# #Nested Class
# class Student:
#     def __init__(self):
#         self.name="abhi"
#         self.J=self.Jenner()

#     def show(self):
#         print(self.name)

#     class Jenner:
#         def __init__(self):
#             self.age=24
#         def show1(self):
#             print(self.age)

# a=Student()
# b=a.Jenner()
# b.show1()

#Inheritance--> class that contain another class that share method and attributes (code reusable)
#parent class-->base class
#child class-->derived class
#MEthod Overriding
'''
class A:
    def show1(self):
        print("this is function1")

class B(A):
    def show2(self):
        print("this is function2")

class C(B):  
    def show3(self):
        super().show2()
        print("this is function 3")

#singlelevel inheritance  A-->B-->C
# a=A()
# a.show1()
b=C()
b.show2()
b.show1()
b.show3()

#multiple inheritance

class A:
    def show1(self):
        print("one")

class B:
    def show2(self):
        print("two")

class C(A,B):
    def show3(self):
        print("three")

a=C()
a.show3()
a.show2()
a.show1()

#POLYMORPHISM

#duck type-->
#method overloading
#method overriding

class Student():
    def show(self):
        print("this is 1st student")

class Teacher:
    def show(self):
        print("this is teacher")
    
def display(var):
    var.show()

a=Student()
b=Teacher()
display(a)
display(b)
'''

#METHOD OVERLOADING

# class Student:
#     def __init__(self,name='',age='') -> None:
#         self.name=name
#         self.age=age
#         print("Welcome")
#     def show(self):
#         print(self.name)
#         print(self.age)
# a=Student("Abhishek")
# a.show()

'''class Student:
    def sum(seld,a=None,b=None):
        s=0
        if a!=None and b!=None:
            s=a+b
        if b!=None and a==None:
            s=b
        elif a!=None and b==None:
            s=a
        else:
            s=None
        return s


var=Student()
print(var.sum(None,2))'''







    








