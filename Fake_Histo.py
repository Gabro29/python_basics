
#Create star histogram 

import random
data=[]
count=0

print(f"Do you want to populate the list with random numbers or do you want to populate it yourself?\n")    #You can pick data from a file too
scelta=input(f"Type R for random or M for manual ")

if scelta == "R":
    
    print(f"Enter the range within which to generate random numbers")
    a=int(input(f"Insert far right "))
    b=int(input(f"Insert far left "))
    items=input(f"How many elements should the list consist of? ")
    
    while count <= int(items):

        number = 0
        number = random.randint(a,b)
        data.append(number)
        count+=1

elif scelta == "M":

    print(f"Insert the data and when finished type finished to not add more data\n")
    
    while True:

        count+=1
        numeber=input(f"Type the {count} number ")

        if number == "Finish":
            break
        else:
            data.append(number)


for i in data:                   #Print Histo

    print(str("*") * int(i))
