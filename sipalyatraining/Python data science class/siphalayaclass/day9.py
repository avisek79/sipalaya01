# #recursive function-function shouldnot call by ourself, it call itself

'''def fact(num):
    if num==0:
        return 0
    
    elif num==1:
        return 1
    
    return num*fact(num-1)'''



# num=int(input("eNTER THE NUMBER :"))
# print(f"the factorial is {fact(num)}")

#List comprehension
a=[1,2,3,4,5,6]
b=[5,7,0,1,8,3]
# c=[]
# for i in a:
#     c.append(i+2)
# print(c)
# v=[i+2 for i in a]
# print(v)
# for i in range(len(a)):
#     c.append(a[i]+b[i])
# print(c)

'''c=[a[i]+b[i] for i in range (len(a))]
print(c)'''

#Local and Global Variable(global variable outside the funtion and local variable inside the function)

# a="python"#Global
# def display():
#     a="django"#local
#     print(a)

# display()
# print(a)


#Lambda-Anonymous Function
#Syntax
# lambda argument:expression

'''v=lambda c:c+2
print(v(4))'''

#Argument more than 

v=lambda x,y:(x+y)/2
print(v(4,6))

# OR
name=int(input("Enter interger :"))
fun=lambda x:x*x*x
print(fun(name))


#What is Git?
'''Control version system-Software or tool. It tracks our projects.
for instances: create, save, re-create, delete, resave,edit
 '''
#Where as github is:
'''store our file or project on remote. It is a website'''



