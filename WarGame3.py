#!/usr/bin/env python
# encoding: utf-8
"""
GameOfWar.py

Created by Neumann, Daniel on 2015-10-06.
Copyright (c) 2015 __MyCompanyName__. All rights reserved.

This is the shell copy. Fill this out to get it to work

"""

import random	

def main():
	"""
	Deck, PlayerAHand and PlayerBHand are all lists
	"""
	
	Deck = []
	PlayerAHand = []
	PlayerBHand = []
	gameCounter = 0

	# Create deck.  Cards are represented by an integer value
	for i in range(52):
		Deck.append(i)
	
	# Shuffle the deck
	random.shuffle(Deck)
	
	# Deal 1/2 the cards to each player
	for x in range(26):
		PlayerAHand.append(Deck.pop())
		PlayerBHand.append(Deck.pop())
	
	# Main Gameplay
	
	while len(PlayerAHand) > 0 and len(PlayerBHand) > 0:
		gameCounter += 1 
		PlayerAHand, PlayerBHand = playRound(PlayerAHand, PlayerBHand)
		if gameCounter % 45 == 0:
			input("pause")
		print(gameCounter)
	
	
	# End of game
	
	print("There were ", gameCounter, " rounds played")
	if len(PlayerAHand) > 0:
	    print ("Player A has won!")
	elif len(PlayerBHand) > 0:
	    print ("Player B has won!")
	else:
	    print ("TIE")

def playRound(PlayerA, PlayerB):
	'''
	This is the method that plays one round of War
	The method takes PlayerA and PlayerB as input parameters
	and returns PlayerA and PlayerB after modification
	for the round
	
	Remember, high card wins. I have included a convenience
	function getRank(anyCard) that will return the rank.
	
	See the README.md for the variations of
	the game to program.
	'''
	
	if getRank(PlayerA[0]) == getRank(PlayerB[0]):
	    return WAR(PlayerA, PlayerB)
	elif getRank(PlayerA[0]) > getRank(PlayerB [0]):
	    PlayerB.pop(0)
	else:
	    PlayerA.pop(0)
	    
	return PlayerA, PlayerB


def WAR(PlayerA, PlayerB):
    # See the README.md file for instructions on coding 
    if len(PlayerA) < 4 and len(PlayerB) < 4:
        PlayerA = []
        PlayerB = []
    elif len(PlayerB) < 4:
        PlayerA.extend(PlayerB)
        PlayerB = []
    elif len(PlayerA) <4:
        PlayerB.extend(PlayerA)
        PlayerA = []
    elif getRank(PlayerA[3]) == getRank(PlayerB [3]):
        PlayerA = PlayerA[4:]
        PlayerB = PlayerB[4:]
    elif getRank(PlayerA[3]) > getRank(PlayerB[3]):
        PlayerA.extend(PlayerB[:4])
        PlayerB = PlayerB[4:]
    else:
        PlayerB.extend(PlayerA[:4])
        PlayerA = PlayerA[4:]
    # This module.
    
    return PlayerA, PlayerB

def getRank(anyCard):
	return anyCard % 13


if __name__ == '__main__':
	main()