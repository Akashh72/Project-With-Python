import random
from turtle import goto
from unittest import result
item=["Stone","Paper","Scissor"]
computer=0
me=0
name=input("Enter Your Name Please : ")
print("\n\n*********Hello {}, Welcome to the game hope you will enjoy this :) ***********\n".format(name))
while(1):
    print("1.Stone\n2.Paper\n3.Scissor\n4.Score\n5.Exit")
    choice=int(input("Enter your choice : "))
    mychoice=""
    if(choice==1):
        mychoice="Stone"
    elif(choice==2):
        mychoice="Paper"
    elif(choice==3):
        mychoice="Scissor"
    elif(choice==4):
        print("\n\nComputer's Score = {}\nYour Score = {}\n\n5".format(computer,me))
        continue
    elif(choice==5):
        print("\nFinal Score : ")
        print("\n\nComputer = {}\nMy score = {}".format(computer,me))
        break
    else:
        print("\n\n!!!!!!!!!!!!Wrong Choice!!!!!!!!!\n\n")
        continue
    print("\n\nStone...Paper...Scissor......\n\n")
    result=random.choice(item)
    print("You = ",mychoice)
    print("Computer = ",result)
    if ((mychoice=="Stone" and result=="Scissor") or (mychoice=="Paper" and result=="Stone") or (mychoice=="Scissor" and result=="Paper")):
        print("\nYou Win\n")
        me+=1
    elif(mychoice==result):
        print("\nDraw Round\n")
    else:
        print("\nComputer Win\n")
        computer+=1
    print("\nLet's Try Again\n")