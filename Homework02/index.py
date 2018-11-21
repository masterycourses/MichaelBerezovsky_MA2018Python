# Testing template for "Guess the number"

###################################################
# Student should add code for "Guess the number" here


# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


import simplegui
import random
import math

def input_guess(guessInput):
    global guessesLeft
    guessesLeft = guessesLeft -1
    guessNumber = int(guessInput)
    print("Guess was "+str(guessNumber))
    print("Number of remaining guesses is "+str(guessesLeft))
    
    if guessNumber == secretNumber:
        print("Correct\nYou win!")
    elif guessNumber > secretNumber:
        print("Lower\n")
    elif guessNumber < secretNumber:
        print("Higher\n")
    else:
        print("Something went wrong")
    if (guessesLeft == 0 and guessNumber != secretNumber):
        print("You ran out of guesses.  The number was "+str(secretNumber))
        new_game(topLimit)
    
def new_game(topLimitParam):
    global secretNumber, guessesLeft, topLimit
    topLimit = topLimitParam
    secretNumber = random.randrange(0, topLimit, 1)
    if topLimit == 100:
        guessesLeft = 7
    else:
        guessesLeft = 10
    print("\nNew game. Range is [0,"+str(topLimit)+")")
    print("Number of remaining guesses is "+str(guessesLeft)+"\n")

def playWithTopLimit(topLimitParam):
    new_game(topLimitParam)
    
def playWithTopLimit100():
    playWithTopLimit(100)
    
def playWithTopLimit1000():
    playWithTopLimit(1000)
    
topLimit = 100
###################################################
# Start our test #1 - assume global variable secret_number
# is the the "secret number" - change name if necessary

playWithTopLimit100()
# secret number is set manually for testcase only. It is random in GUI
secretNumber = 74

input_guess("50")
input_guess("75")
input_guess("62")
input_guess("68")
input_guess("71")
input_guess("73")
input_guess("74")

###################################################
# Output from test #1
#New game. Range is [0,100)
#Number of remaining guesses is 7
#
#Guess was 50
#Number of remaining guesses is 6
#Higher!
#
#Guess was 75
#Number of remaining guesses is 5
#Lower!
#
#Guess was 62
#Number of remaining guesses is 4
#Higher!
#
#Guess was 68
#Number of remaining guesses is 3
#Higher!
#
#Guess was 71
#Number of remaining guesses is 2
#Higher!
#
#Guess was 73
#Number of remaining guesses is 1
#Higher!
#
#Guess was 74
#Number of remaining guesses is 0
#Correct!
#
#New game. Range is [0,100)
#Number of remaining guesses is 7

###################################################
# Start our test #2 - assume global variable secret_number
# is the the "secret number" - change name if necessary

playWithTopLimit1000()
# secret number is set manually for testcase only. It is random in GUI
secretNumber = 375
#secret_number = 375	
input_guess("500")
input_guess("250")
input_guess("375")

###################################################
# Output from test #2
#New game. Range is [0,100)
#Number of remaining guesses is 7
#
#New game. Range is [0,1000)
#Number of remaining guesses is 10
#
#Guess was 500
#Number of remaining guesses is 9
#Lower!
#
#Guess was 250
#Number of remaining guesses is 8
#Higher!
#
#Guess was 375
#Number of remaining guesses is 7
#Correct!
#
#New game. Range is [0,1000)
#Number of remaining guesses is 10



###################################################
# Start our test #3 - assume global variable secret_number
# is the the "secret number" - change name if necessary

playWithTopLimit100()
#secret_number = 28	
secretNumber = 375
input_guess("50")
input_guess("50")
input_guess("50")
input_guess("50")
input_guess("50")
input_guess("50")
input_guess("50")

###################################################
# Output from test #3
#New game. Range is [0,100)
#Number of remaining guesses is 7
#
#Guess was 50
#Number of remaining guesses is 6
#Lower!
#
#Guess was 50
#Number of remaining guesses is 5
#Lower!
#
#Guess was 50
#Number of remaining guesses is 4
#Lower!
#
#Guess was 50
#Number of remaining guesses is 3
#Lower!
#
#Guess was 50
#Number of remaining guesses is 2
#Lower!
#
#Guess was 50
#Number of remaining guesses is 1
#Lower!
#
#Guess was 50
#Number of remaining guesses is 0
#You ran out of guesses.  The number was 28
#
#New game. Range is [0,100)
#Number of remaining guesses is 7

gameFrame = simplegui.create_frame("Guess Number Game", 300, 300)
gameFrame.add_input("Guess Number", input_guess, 100)
gameFrame.add_button("Rangeis[0,100)", playWithTopLimit100, 150)
gameFrame.add_button("Rangeis[0,1000)", playWithTopLimit1000, 150)
gameFrame.start()

# new game is called after GUI start to ensure that thare is a new game regardless
# of hardcoded test runs. If hardcoded tests were run then game is initialized twice
# and with range from previous run. If no tests have been run then range is [0,100)

new_game(topLimit)