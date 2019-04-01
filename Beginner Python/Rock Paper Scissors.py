import random

print("Rock, Paper, Scissors\n\n")
counter = 0
myScore = 0
botScore = 0

while counter < 6:
    rock = 'rock'
    paper = 'paper'
    scissors = 'scissors'
    bot_choice = [rock,paper,scissors]
    botChoice = random.choice(bot_choice)
   
    playGame = input("rock, paper or scissors?\n")
    if(playGame == 'rock'):
        if botChoice == rock:
            print("No winner, its a draw\n")
            counter+=1
        elif botChoice == paper:
            print("You lose! The bot chooses paper!\n")
            counter+=1
            botScore+=1
        elif botChoice == scissors:
            print("You win! The bot chose scissors\n")
            counter+=1
            myScore+=1
    elif(playGame == 'paper'):
        if botChoice == rock:
            print("You win! The bot chose rock\n")
            counter+=1
            myScore+=1
        elif botChoice == paper:
            print("No winner, its a draw\n")
            counter+=1
        elif botChoice == scissors:
            print("You lose! The bot chose scissors\n")
            counter+=1
            botScore+=1
    elif(playGame == 'scissors'):
        if botChoice == rock:
            print("You lose! The bot chose rock\n")
            counter+=1
            botScore+=1
        elif botChoice == paper:
            print("You win! The bot chose paper\n")
            counter+=1
            myScore+=1
        elif botChoice == scissors:
            print("No winner! Its a draw\n")
            counter+=1

    if counter == 6:
        if myScore < botScore:
            print("The bot wins!\n")
        elif myScore > botScore:
            print("You win!\n")
        else:
           print("It was a tie!\n")
            
    
