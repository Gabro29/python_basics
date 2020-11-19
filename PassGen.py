
#Password generator

import random

chars=open("ascii.txt", "r").readlines()      #You can add other ascii
password=""
alfanum=""
temp=0

print(f"\nDo you want to generate a simple password with alphanumeric characters or complicated with ASCII characters?\n")
scelta=input(f"Type S for a simple one or C for complicated ")

if scelta== "S":

    for i in range(22,84):      #Pick up only alphanumerica characters

        alfanum+=chars[0][i]
        
    for j in range(0,8):        #Pass gen with the random library

        password+=random.choice(alfanum)

elif scelta == "C":         #Pick up all chars in the txt file

    for i in range(0,20):

        temp=random.randrange(94)
        password+=chars[0][temp]
    
print(f"Here it is----> {password}")



