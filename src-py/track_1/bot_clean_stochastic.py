'''
Created on Mar 27, 2013

@author: anuvrat
'''

#!/usr/bin/python

# Head ends here
def distance_to_dirt(bot_x, bot_y, board):
    for x_idx in range(5):
        for y_idx in range(5):
            if board[x_idx][y_idx] != 'd': continue
            dirt_x = x_idx
            dirt_y = y_idx
            break
    
    return bot_x - dirt_x, bot_y - dirt_y

def nextMove(posx, posy, board):
    x_dist, y_dist = distance_to_dirt(posx, posy, board)
    
    if x_dist == 0 and y_dist == 0: print('CLEAN')
    elif y_dist == 0:
        print('UP' if x_dist > 0 else 'DOWN')
    else:
        print('LEFT' if y_dist > 0 else 'RIGHT')

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)