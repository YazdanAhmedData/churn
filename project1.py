import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([-1,0,1])
youstr =input("enter your choice:")
youdict = {"snake":1,"water":-1,"gun":0}
reversedict= {1:"snake",-1:"water",0:"gun"}

you =youdict[youstr]

print(f"Computer choose {reversedict[computer]}\nYou choose {reversedict[you]}") 

if(computer == you):
    print("its a draw")
else:
    if(computer == -1 and you == 1):
        print("you win!")
    elif(computer == -1 and you == 0):
        print("you lose!")
    elif(computer == 1 and you == -1):
        print("you lose!")
    elif(computer == 1 and you == 0):
        print("you win!")
    elif(computer == 0 and you == -1):
        print("you win!")
    elif(computer == 0 and you == 1):
        print("you lose!")
    else:
        print("something went wrong")

