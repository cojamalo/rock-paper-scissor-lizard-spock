#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 12:57:32 2017

@author: cojamalo
"""

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

import math
import random as rand

# helper functions

def name_to_number(name):
    # Create dictionary for the name:code mapping
    choices = {
        'rock': 0,
        'Spock': 1,
        'paper': 2,
        'lizard': 3,
        'scissors': 4
            }
    # Check if name is in the dictionary
    if name in choices:
        return choices[name] # If so, return the code
    else:
        return -1 # If not, return error code

def number_to_name(number):
    # Create dictionary for the name:code mapping
    choices = {
        0:'rock',
        1:'Spock',
        2:'paper',
        3:'lizard',
        4:'scissors'
            }
    # Check if code is in the dictionary
    if number in choices:
        return choices[number] # If so, return the name
    else:
        return -1 # If not, return error code

def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print("")
    # print out the message for the player's choice
    print("Player chooses " + player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = rand.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print("Computer chooses "+comp_choice)
    # compute difference of comp_number and player_number modulo five
    diff = (comp_number - player_number) % 5
    # use if/elif/else to determine winner, print winner message
    
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


