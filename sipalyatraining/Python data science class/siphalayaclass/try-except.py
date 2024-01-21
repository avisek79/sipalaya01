#exception Handling -->
'''
syntax
    try:
        code---------
    except
        code-----------
'''
# try:
#     a=int(input("Enter any integers :"))
#     b=int(input("Enter any integers :"))
#     def show(a,b):
#         s=a+b
#         print(s)
#         str1="Abhishek"
#         print(str1[9])
       
#     show(a,b)

# # except:
# #      k=0/0
# #      print(k)
# #      print("you have to enter an integers")

# except IndexError:
#     print("please input valid index")

# except ValueError:
#     print("you got an value error")

# except ZeroDivisionError:
#     print("you cannto divide by zero")

# finally:
#    print("Our next important code is here")



def show():
    try:
        num=int(input("enter your number :"))
        s=num**2
        return s
    except:
        print("got an error")
        return 0
    finally:
        print("this code is important")
print(show())

