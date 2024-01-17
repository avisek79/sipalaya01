# #While Loop 
# var_1=1
# while var_1<=10:
#     print(var_1)
#     var_1 += 2

# #for infinite loop {press (Ctrl+C)}
    
# while True:
#     print("this is infinitve loop")

# you can use else also
    
#Conditional statement
#break

# a=1
# while a<10:
   
#     a +=1
#     if a==6:
#         continue
#     print(a)
        
    

# for i in range(10):
#     if i%2==0:
#         continue
#     print(i)

# #pass
# for i in range(10):
#     pass

#guessing game

# a="abhishek"
# guess=" "
# count=1
# limit=3

# while guess!=a:
#     guess=input("guess word :")
#     count+=1

#     if count==limit:
#         print("game over")
#         break
# else:
#     print("you won!")


#FUNCTIONS-block of codes which does specific task only after calling this function

#Syntax

# def function_name(arg-->formal_argument):
#     #block of code

# function_name(arg-->actual_argument)

# def show(name,age):
#     print(f"Hallo herr {name}! and my age is {age}")
#     print("hallo Herr wicker, wie geht as dir?")
#     pass

# name=input("please input your name and age")
# age=input()
# show(name,age)

#H|W
# fibonacci series

#calculate max and min
a=[2,4,3,6,7,8,8,8,7,5,3,3,6,6,5,44,34,15,89,98,67,64,34,32,50,99,91]
k=[]
l=[]
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            
            a[i],a[j]=a[j],a[i]

        elif a[i]<a[j]:
          a[i],a[j]=a[i],a[j]

        
print(a)

print(" ")
print(f"The maximum value in the list is {a.pop()}")
print(" ")
print(f"the minimum value is {a[0]}")






            


    