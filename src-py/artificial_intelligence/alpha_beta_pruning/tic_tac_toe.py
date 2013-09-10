'''
Created on Nov 6, 2012

@author: anuvrat
'''

#!/bin/python
import re

x_win_pattern = re.compile( r'([X]{3}.{6}|.{3}[X]{3}.{3})|.{6}[X]{3}|(X.{2}){3}|(.X.){3}|(.{2}X){3}|X.{3}X.{3}X|.{2}X.X.X.{2}' )
o_win_pattern = re.compile( r'([O]{3}.{6}|.{3}[O]{3}.{3})|.{6}[O]{3}|(O.{2}){3}|(.O.){3}|(.{2}O){3}|O.{3}O.{3}O|.{2}O.O.O.{2}' )

def not_player( player ):
    if player == 'X': return 'O'
    elif player == 'O': return 'X'
    else: return '_'

def eval_board( board ):
    if x_win_pattern.match( board ): return 'X'
    elif o_win_pattern.match( board ): return 'O'
    else: return '_'

def next_move( player, board ):
    valuation, empty_slots = eval_board( board ), board.count( '_' )
    if empty_slots == 0 or ( valuation != '_' and player != valuation ): return valuation, board, -1

    loc = -1
    drawn_boards, loss_boards, drawn_board_loc, loss_board_loc = [], [], [], []
    for _ in xrange( empty_slots ):
        loc = board.find( '_', loc + 1 )
        new_board = board[:loc] + player + board[loc + 1:]
        res, _, _ = next_move( not_player( player ), new_board )
        if player == res: return player, new_board, loc
        elif res == '_':
            drawn_boards.append( new_board )
            drawn_board_loc.append( loc )
        else:
            loss_boards.append( new_board )
            loss_board_loc.append( loc )

    if len( drawn_boards ) != 0: return '_', drawn_boards[0], drawn_board_loc[0]
    else: return not_player( player ), loss_boards[0], loss_board_loc[0]

def nextMove( player, board ):
    _, _, move_played = next_move( player, "".join( board ) )
    print move_played / 3, move_played % 3


# If player is X, I'm the first player.
# If player is O, I'm the second player.
player = raw_input()

# Read the board now. The board is a 3x3 array filled with X, O or _.
board = []
for i in xrange( 0, 3 ):
    board.append( raw_input() )

nextMove( player, board );

