a=int(input("Enter the number to check whether it is prime or not !"))

if a==1:
    print(f"{a} is a prime number.")
n=2
count=0
while n<a:
    if a%n==0:
        count+=1
        # break
    n +=1

if count>=1:
    print("the number is not a prime")
else:
    print("prime")
# else:
#     print("it is not a prime number")

   


    
    

