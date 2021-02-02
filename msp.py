# MSP Hangman
# Written by Asha Gupta

import random   #generates random word

words = ["cake", "brownie", "pizza", "hamburger", "sushi"]
 
aWord = words[random.randint(0,len(words)-1)]  #chooses random word
answerList = []   
lives = 6   #number of lives
letterInput = " " 
rightGuess = 0  #number of correct guesses
winLose = None  #set to true or false, ends game with message 
mspState=0   #sets tate of the drawing
uniqueChar=len(set(aWord))   #finds the amount of unique letters
for x in range(len(aWord)):  #makes the array as long as the answer
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
	if letterInput in aWord:
		print("That's right!")

		for x in range(len(answerWord)): 
<<<<<<< HEAD
            		if letterInput == aWord[x]:
                		answerList[x] = letterInput
=======
            		if letterInput == aWord[x]:
                		answerList[x] = letterInput # if answer is right adds letter in array
>>>>>>> 9dc518e89cfb73fbf08da7c6c89101090ed2f590
		print(answerList)
		rightGuess = rightGuess + 1 
		msp(mspState) # shows hangman state after each round

		if rightGuess == uniqueChar: 
			winLose = True
			break # if all letters are guessed end game

	else:
		lives = lives-1 
		print("That's Wrong!")
		msp(mspState)
		mspState = mspState + 1 # if wrong add to the hangman 
	if winLose == True:
		print ("Winner")
	else: 
		print("Lost!")


