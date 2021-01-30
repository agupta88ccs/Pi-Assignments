# MSP Hangman
# Written by Asha Gupta

import random   #generates random word

words = ["cake", "brownie", "pizza", "hamburger", "sushi"]
 
answerWord = words[random.randint(0,len(words)-1)]  #chooses random word
answerList = []   
lives = 6   #number of lives
letterInput = " " 
rightGuess = 0  #number of correct guesses
winLose = None  #set to true or false, ends game with message 
mspState=0   #sets tate of the drawing
uniqueChar=len(set(answerWord))   #finds the amount of unique letters
for x in range(len(answerWord)):  #makes the array as long as the answer
    answerList.extend('_') 

def msp(mspState):  #the hangman drawings
  if mspState == 0:
        print(" ")
        print("---|")
        print(" ")
  if mspState == 1:
        print(" ")
        print("---|")
        print("   0")
        print(" ")
  if mspState == 2:
        print(" ")
        print("---|")
        print("   0")
        print("  / ")
        print(" ")
  if mspState == 3:
        print(" ")
        print("---|")
        print("   0")
        print("  /|")
        print(" ")
  if mspState == 4:
        print(" ")
        print("---|")
        print("   0")
        print("  /|\ ")
        print(" ")
  if mspState == 5:
        print(" ")
        print("---┐")
        print("   0")
        print("  /|\ ")
        print("  /  ")
        print(" ")
  if mspState == 6:
        print(" ")
        print("---|")
        print("   0")
        print("  /|\ ")
        print("  / \ ")
        print(" ")

print ("Lets play Hangman!")

while lives>0:
	letterInput = input("Enter a letter: ")
	if letterInput in answerWord:
		print("That's right!")

		for x in range(len(answerWord)): 
            		if letterInput == answerWord[x]:
                		answerList[x] = letterInput
		print(answerList)
		rightGuess = rightGuess + 1
		msp(mspState)

		if rightGuess == uniqueChar:
			winLose = True
			break

	else:
		lives = lives-1
		print("That's Wrong!")
		msp(mspState)
		mspState = mspState + 1
	if winLose == True:
		print ("Winner")
	else: 
		print("Lost!")


