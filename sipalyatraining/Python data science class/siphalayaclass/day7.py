#While Loop and for loop

for i in range(10,0,-1):
    print(i)
    if i==1:
        print("go")

#multiplication table
        
num=int(input("enter the value for the multiplication :"))
print(" ")
print("here is your multiplication table :")
for i in range (1,11):
    k=i*num
    
    print(f"{num} x {i} = {k}")

#addition using for loop (question for interview)
    
a=[2,3,4,5,6]
b=[]
for i in a:
    b.append(i+2)
print(b)

#short handed statement (interview questions)
print("your age is smaller than ram") if 20<25 else print("you are fit")


# For Loop Palindrome number
a=["141","nayan","1234321","phone"]
# print(a[:])
for i in a:
    if i==i[::-1]:
        print(f"{i} is palindrome number/word.")
    else:
        print(f"Sorry {i} is not palindrome")
# if a==a[::-1]:
#     print("yes")
    
# else:
#     print("no")
        
for i in range(6):
    for j in range(i):
        print(f"{j}",end=" ")
    print("")

# for i in range(1):
    
#     print(i)
