'''
Created on Mar 27, 2013

@author: anuvrat
'''

grid_size = 5
dirts = []
preprocess_done = 0
selected_dirt_idx = -1

def find_all_dirts(board):
    for x_idx in range(grid_size):
        for y_idx in range(grid_size):
            if board[x_idx][y_idx] == 'd': dirts.append([x_idx, y_idx])
    
    global preprocess_done
    preprocess_done = 1

def find_closest_dirt(bot_x, bot_y):
    min_dist = 9
    for idx in range(len(dirts)):
        dirt = dirts[idx]
        dist_x = bot_x - dirt[0] if bot_x > dirt[0] else dirt[0] - bot_x
        dist_y = bot_y - dirt[1] if bot_y > dirt[1] else dirt[1] - bot_y
        dist = dist_x + dist_y
        if dist < min_dist:
            min_idx = idx
            min_dist = dist
    
    global selected_dirt_idx
    selected_dirt_idx = min_idx

def clean():
    global selected_dirt_idx
    dirts.pop(selected_dirt_idx)
    selected_dirt_idx = -1

def print_next_move(bot_x, bot_y):
    dirt_x = dirts[selected_dirt_idx][0]
    dirt_y = dirts[selected_dirt_idx][1]

    if bot_x == dirt_x and bot_y == dirt_y:
        clean()
        print('CLEAN')
    elif bot_x > dirt_x: print('UP')
    elif bot_y > dirt_y: print('LEFT')
    elif bot_x < dirt_x: print('DOWN')
    else: print('RIGHT')

# Head ends here
def next_move(posx, posy, board):
    if preprocess_done == 0: find_all_dirts(board)
    
    if selected_dirt_idx == -1: find_closest_dirt(posx, posy)
    
    print_next_move(posx, posy)

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)