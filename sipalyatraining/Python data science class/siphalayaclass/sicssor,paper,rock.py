#Scissor, Paper and Rock
a="Welcome to scissor, Paper and Rock game"
print(a.center(80,"-"))
print(" ")
print("for your information:")
denotation='''
            S for "scissor",
            R for "Rock" and 
            P for "Paper" '''
print(denotation)
print(" ")
user=input("enter your choice : ")
user=user.upper()

if user not in ["S","R","P"]:
    print("Invalid Syntax, please try again later")
    quit()

print(f"you have choosen \"{user}\".")

import random

computer_choice=random.choice(["R","P","S"])
print(f"computer choice is : \"{computer_choice}\"")

if (user=="S" and computer_choice=="P") or (user=="R" and computer_choice=="S") or \
    (user=="P" and computer_choice=="R"):
    print("CONGRATULATION!! You Won The Game")

elif user==computer_choice:
    print("Draw!!")

else:
    print("Sorry! Computer Won the Game")







