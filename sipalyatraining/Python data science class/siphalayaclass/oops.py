'''#OOPS
#1. Procedure
#---#OOPS----# --> variable haru lai real world entity ma match garxa
#oops is used class and object lai use garxa'''

#Class-->( blueprint of object or collection of object)
#object-->instance of class
#Self- self le current object lyauxa. It is not a reserved keyword.
#instance variable= variable 
#instance variable acess instance method which contain self parameter in it first program

'''StudentForm-->class[blueprint]
Ram-->Ram ko Information --object
Abhishek--> Abhishek ko information --object[instance]'''

#Class --> group of attribute and method
#Attribute-->Represent varaible which holds data
#Method -->Similar to function, perform a action or Task
#asset=assert condition, error message

# # SYNTAX:
# class ClassName:
#     def __init__(self) -> None:     #Method
#         # self.variable_name="Abhishek" #Attribute
#         # self.variable_age=24    #Attribute
#         print("Helllo world")

#     def show(self):
#         # print(self.variable_age,self.variable_name)
#         print("this wont get run")
# a=ClassName() #Object
# a.show()

# class Student:
#     def __init__(self,name):
#         self.name=name

#     def show(self,age):
#         print(f"my name is {self.name} and my age is {age}")

# a=Student("Abhishek")
# a.show(24)

class Shop:
    bonus=0.1
    def __init__(self,name,price:int,qty:int):
        #Validation
        assert qty>=0 , f"quanitity {qty} should be greater than zero"
        assert price>=0 , f"price {price} should be greater than zero"
        self.name=name
        self.price=price
        self.quantity=qty

    def TotalPrice(self):
        return self.price*self.quantity
    
obj1=Shop("Alchemist",350,50)
print(f"The total price of Alchemist book is {obj1.TotalPrice()} \n and")

obj2=Shop("pen",256,406)
print(f"The total price of pens are {obj2.TotalPrice()}")










