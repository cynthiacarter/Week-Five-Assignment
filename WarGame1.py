# WarGame1.py
# Cynthia Carter
# Intro to CS 125
# A program that simulates the card game War

#players
a = []
b = []

#playing deck
for cards in range (52):
   deck.append(cards)
 
#shuffle deck
import random
random. shuffle (deck)

#deal deck
for x in range (26):
    a.append(deck.pop())
    b.append(deck.pop())

#main game
while len(a) > 0 and len (b) > 0:
    deck +=1
    a,b = gameCounter (a,b)
 
#print score

print ("There were", gameCounter, " rounds played")

# Define

return a,b

def getRank (anycard):
    return anycard %13
    
if name =='main'
    main()