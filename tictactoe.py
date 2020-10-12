"""
Tic Tac Toe Player
"""

import math
import copy
import numpy as np

X = "X"
O = "O"
EMPTY = None

def initial_state():
    # Returns starting state of the board.

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    # Returns player who has the next turn on a board.
    # X are positive - O are negative
    # raise NotImplementedError
    vsum = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X :
                vsum = vsum + 1
            elif  board[i][j] == O :
                vsum = vsum - 1
    if vsum <= 0:
        return X
    else:
        return  O

def actions(board):
    # Returns set of all possible actions (i, j) available on the board.
    Choose = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                Choose.append([i,j])
    return Choose

def result(board, action):
    # Returns the board that results from making move (i, j) on the board.
    board[action[0]][action[1]] = player(board)
    return board

def winner(board):
    # Returns the winner of the game, if there is one.
    if Score(X, board) == 1:
        return X
    elif Score(O, board) == 1:
       return O    
    else:    
        return None

def utility(board):
    #    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    if Score(X, board) == 1:
        return 1
    elif Score(O, board) == 1:
       return -1
    else:    
        return 0

def terminal(board):
    # Returns True if game is over, False otherwise.    
    SomeOneWon =  utility(board) in [1,-1]   
    return SomeOneWon or (actions(board) == [])

def Score(player, board):
    # Returns the score of the player
    mat = np.zeros((3,3))

    for i in range(3):
        for j in range(3):
            if board[i][j] == player:
                mat[i][j] = 1
  
    if ((3 in mat.sum(axis = 0)) or (3 in mat.sum(axis = 1)) or (3 == sum(mat.diagonal())) or (3 == sum(np.fliplr(mat).diagonal())) ):
        return 1
    else:
        return 0  

def minimax(board):
    # Returns the optimal action for the current player on the board.
    if board == initial_state():
        return(1,1)

    res = []
    Hypotetical = copy.deepcopy(board)

    Poss = actions(Hypotetical)

    if player(board) == O:
        for action in Poss:
            res.append( MinValue(result(copy.deepcopy(Hypotetical), action))) 

        return Poss[res.index(min(res))] 
    else:
        for action in Poss:
            res.append( MaxValue(result(copy.deepcopy(Hypotetical), action))) 

        return Poss[res.index(max(res))] 

def MinValue(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    
    for action in actions(board):
        v = min(v, MaxValue(result(copy.deepcopy(board),action)))    
    return v  
    
def MaxValue(board):
    if terminal(board):
        return utility(board)
    v = -math.inf

    for action in actions(board):
        v = max(v, MinValue(result(copy.deepcopy(board), action)))    
    return v 
