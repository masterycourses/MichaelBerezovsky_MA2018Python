# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random

def name_to_number(name):
    result = -1
    if name is None:
        print("name argument is empty")
    elif name == "rock":
        result = 0
    elif name == "Spock":
        result = 1
    elif name == "paper":
        result = 2
    elif name == "lizard":
        result = 3
    elif name == "scissors":
        result = 4
    else:
        print("name argument is not valid")
        result = -2
    return result


def number_to_name(number):
    result = "Invalid"
    if number is None:
        print("provided bumber is empty")
    elif number == 0:
        result = "rock"
    elif number == 1:
        result = "Spock"
    elif number == 2:
        result = "paper"
    elif number == 3:
        result = "lizard"
    elif number == 4:
        result = "scissors"
    else:
        result = "Number is out of range"
        print(result)
    return result
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    print("\n")
    print("Player chooses: " + player_choice)
    playersChoiceNumber = name_to_number(player_choice)
    opponentChoiceNumber = random.randrange(0, 5, 1)
    opponentChoiceName = number_to_name(opponentChoiceNumber)
    print("Computer chooses: " + opponentChoiceName)
    resultDiff = (opponentChoiceNumber - playersChoiceNumber) % 5
    winnerName = "draw"
    if resultDiff == 0:
        winnerName = "nobody. It is a draw"
    elif resultDiff < 3:
        winnerName = "computer"
    else:
        winnerName = "player"
    print("Winner is: " + winnerName)

    
random.seed()
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
