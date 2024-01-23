#second largest number from the list
list1=[3,7,1,13,18,23,8,16,21,28,25,4,9]
for i in range(len(list1)+1):
    for j in range(i+1,len(list1)):
        if list1[i]<list1[j]:
            list1[i],list1[j]=list1[i],list1[j]

        elif list1[i]>list1[j]:
            list1[i],list1[j]=list1[j],list1[i]

print(list1[len(list1)-2])

import random
#display all prime numbers
prime_numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


valid_prime_numbers=[1]
for i in prime_numbers:
    count=0
    for j in range(2,i+1):
        if i%j==0:
            count +=1
    if count==1:
        valid_prime_numbers.append(i)
    
print(f"the prime numbers are {(valid_prime_numbers)}")

#fibonacci series

def fib(a,b):
    sum=[a,b]
    for i in range(18):
        c=a+b
        a=b
        b=c
        sum.append(c)
    print("the fibonaccci series is",sum)
a=0
b=1
fib(a,b)

#Multiplication table

def Mul(num):
    for i in range(1,11):
        print(f"{num} X {i} = {num*i}")

num=int(input("Enter any number"))
Mul(num)


#descending order all odd appearing before all even number

list_1=[1,2,3,4,5,6,7,8,9,10,11,12,13,16,18,24,14,46,33,28,29,22,56,67,45,88]
list_odd=[]
list_even=[]
list_sorted=[]
list_sorted_1=[]
for i in range(len(list_1)):
    # for j in range(i+1, len(list_1)):
        if list_1[i]%2!=0:
            list_odd.append(list_1[i])
# print(list_odd)
list_odd.sort()
# print(list_odd)
list_odd=list_odd[::-1]
list_sorted.extend(list_odd)
print(list_sorted)
                   

for j in range(len(list_1)):
      if list_1[j]%2==0:
            list_even.append(list_1[j])
# print(list_even)
list_even.sort()
# print(list_even)
list_even=list_even[::-1]

list_sorted_1.extend(list_even)
print(list_sorted_1)

# list_concatinated=",".join(map(str,(list_sorted+list_sorted_1)))
list_concatinated=list_sorted+list_sorted_1

print(" ")
print("the final output is",list_concatinated)

        

