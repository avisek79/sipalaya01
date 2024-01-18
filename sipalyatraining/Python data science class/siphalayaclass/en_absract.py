#encapsulation-->wraping method and data in a unit(class)
'''
class S:
    def __init__(self) -> None:
        self.name="Robert"
a=S()
print(a.name)

class T:
    def __init__(self) -> None:
        print(a.name)

b=T()

#it uses private and protect to restrict from globally
    #_name=(protected)
    #__name=(private)

class Student:
    __name="murp" #private
    _age=23 #protect
    def show(self):
        print(self.__name)
        print(self._age)

a=Student()
a.show()

# print("my name is ", a.__name)
print("my age is ", a._age)'''

#ABSTRACTION
#--> Hiding complexity from user:only show service

def sumation():
    a=int(input("Enter your first number :"))
    b=int(input("Enter your second number :"))
    s=a+b
    print(f"the sume is {s}")

# sumation()