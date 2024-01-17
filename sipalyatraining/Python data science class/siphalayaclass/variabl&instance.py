'''class Student:
    def __init__(self) -> None:
        self.name="Abhishek" #instance variable

    def show(self): #instance method
        print(self.name) #instance variable acess innside class

a=Student()
a.name="Potter" #instance varailbe acess outside the class -->objectName.instance variable (INSTANT METHOD)
a.show()

b=Student()
b.show() '''

#CLASS VARIABLE -->variable which have single copy of every object
#Class method -->acess class variable with cls in first argument
class Student():
    school="MSBS"
    def __init__(self) -> None:
        self.name="Abhishek"

    # @classmethod #decorator
    @staticmethod
    def show(): #class method
        print(f"hey its me") #class variable acess inside class

a=Student()
Student.school="Siddhartha"
a.show()

b=Student()
b.show()


