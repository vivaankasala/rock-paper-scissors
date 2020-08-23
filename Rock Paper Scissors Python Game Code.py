# -*- coding: usf-8 -*-
"""
Created on Sun Aug 23 15:03:43 2020

@author: Manav & Vivaan
"""
from random import randint

#create a list of play options
s = ["Rock", "Paper", "Scissors"]

#assign a random play to the AI
AI = s[randint(0,2)]

#set You to False
You = False

while You == False:
#set You to True
    You = input("Rock, Paper, Scissors?")
    if You == AI:
        print("Tie!")
    elif You == "Rock":
        if AI == "Paper":
            print("You lose!", AI, "covers", You)
        else:
            print("You win!", You, "smashes", AI)
    elif You == "Paper":
        if AI == "Scissors":
            print("You lose!", AI, "cut", You)
        else:
            print("You win!", You, "covers", AI)
    elif You == "Scissors":
        if AI == "Rock":
            print("You lose...", AI, "smashes", You)
        else:
            print("You win!", You, "cut", AI)
    else:
        print("That's not a valid play. Check your spelling!")
    #You was set to True, but we want it to be False so the loop continues
    You = False
    AI = s[randint(0,2)]