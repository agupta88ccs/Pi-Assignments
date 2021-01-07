# Automatic Dice Roller
# Written by Asha Gupta

from random import randint 

print ("Automatic Dice Roller")
repeat = True #repeats function if true
while repeat:
    print("You rolled",randint(1,6)) #prints your number, sets range 
    print("Roll again?")
    repeat = ("y" or "yes") in input().lower() #repeats function if yes
