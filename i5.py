'''i=1
while(12<i<20):
	print(i)'''
	
"""a=float(input("Enter a Number:"));
if(a%2==0):
	print("This Number is Even")
else:
	print("This Number is Odd")"""
'''import random
r=random.randint(1,6)
print(r)'''

'''import random
while True :
	a=input("press t")'''

"""for i in range(1,100):
	for j in range(1,100):
		print(i,'x',j,"=",i+j)"""

'''import random
a=(1:'r',2:'p',3:'s')

while True
	p=input("your choice r/p/s:")
	c=a(random.randit(1,3))
print("your choice ",p," compuuter choice ",c,")

		if(p==c):
		print("draw")
elif (p=="r")'''

from random import randint
 
#create a list of play options
t = ["Rock", "Paper", "Scissors"]
 
#assign a random play to the computer
computer = t[randint(0,2)]
 
#set player to False
player = False
 
while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]







