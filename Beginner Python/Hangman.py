import time
import random

def hangMan():

    hangman = 0
    word1 = 'tray'
    word2 = 'kite'
    word3 = 'sand'
    word4 = 'card'
    wordBank = [word1, word2 , word3 , word4]
    wordChoice = random.choice(wordBank)
    wordLength = len(wordChoice)

    hung = 0

    while hung == 0:
        print("HANGMAN" "\n" "The word I am thinking of has", wordLength, "letters in it" "\n")
        letter_guess = input("Guess a letter or the word: ")

        if letter_guess == wordChoice[0] or letter_guess == wordChoice[1] or letter_guess == wordChoice[2] or letter_guess == wordChoice[3]:
            print("Correct! There is a", letter_guess, "in the word!" "\n")
            print(letter_guess)
        elif letter_guess == wordChoice:
            print("Congrats!! You solved the puzzle ya smarty pants!!" "\n")
            break
        else:
            print("I am sorry. But that is wrong. The HEAD is now drawn" "\n")
            hung += 1

    while hung == 1:
        print("The word I am thinking of has", wordLength, "letters in it" "\n")
        letter_guess2 = input("Guess a letter or the word: ")

        if letter_guess2 == wordChoice[0] or letter_guess2 == wordChoice[1] or letter_guess2 == wordChoice[2] or letter_guess2 == wordChoice[3]:
            print("Correct! There is a", letter_guess2, "in the word!" "\n")
            print(letter_guess2)
        elif letter_guess2 == wordChoice:
            print("Congrats!! You solved the puzzle ya smarty pants!!" "\n")
            break
        else:
            print("I am sorry. But that is wrong. The BODY is now drawn" "\n")
            hung += 1

    while hung == 2:
        print("The word I am thinking of has", wordLength, "letters in it" "\n")
        letter_guess3 = input("Guess a letter or the word: ")

        if letter_guess3 == wordChoice[0] or letter_guess3 == wordChoice[1] or letter_guess3 == wordChoice[2] or letter_guess3 == wordChoice[3]:
            print("Correct! There is a", letter_guess3, "in the word!" "\n")
            print(letter_guess3)
        elif letter_guess3 == wordChoice:
            print("Congrats!! You solved the puzzle ya smarty pants!!" "\n")
            break
        else:
            print("I am sorry. But that is wrong. The ARMS are now drawn" "\n")
            hung += 1

    while hung == 3:
        print("The word I am thinking of has", wordLength, "letters in it" "\n")
        letter_guess4 = input("Guess a letter or the word: ")

        if letter_guess4 == wordChoice[0] or letter_guess4 == wordChoice[1] or letter_guess4 == wordChoice[2] or letter_guess4 == wordChoice[3]:
            print("Correct! There is a", letter_guess4, "in the word!" "\n")
            print(letter_guess4)
        elif letter_guess4 == wordChoice:
            print("Congrats!! You solved the puzzle ya smarty pants!!" "\n")
            break
        else:
            print("I am sorry. But that is wrong. The LEGS are now drawn" "\n")
            hung += 1

    if hung == 4:
        time.sleep(1)
        print("I AM SORRY. BUT YOU HAVE BEEN HUNG :( ")
        time.sleep(3)
        quit()

hangMan()
        
