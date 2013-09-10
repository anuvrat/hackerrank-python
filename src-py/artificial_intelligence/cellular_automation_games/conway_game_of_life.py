'''
Created on Dec 31, 2012

@author: anuvrat
'''
import random

pattern = [145, 147, 118, 91, 62, 33, 64, 35, 6, 36]
locations = [150, 585, 600, 165]

def nextMove( player, board ):
    iteration = board.count( player )
    loc, idx = iteration / 10, iteration % 10

    position = locations[loc] + pattern[idx]
    while board[position] != '-' :
        position = random.randint( 0, 625 )

    return position / 29, position % 29

# Tail starts here
player = raw_input()
board = ""
for i in xrange( 0, 29 ):
    board += raw_input()

a, b = nextMove( player, board )
print a, b
