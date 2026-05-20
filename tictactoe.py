"""
Tic Tac Toe Player
"""

import math
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_counter = 0
    o_counter = 0
    for line in board:
        for cell in line:
            if cell == X:
                x_counter+=1
            elif cell ==O :
                o_counter+=1
    if o_counter<x_counter:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                possible_moves.append((i,j))
    return tuple(possible_moves)


import copy
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    x,y = action
    player_to_move  = player(board)
    board_copy = list()
    board_copy = copy.deepcopy(board)
    board_copy[x][y] = player_to_move
    return board_copy

def win_condition(board,player):
    """
    returns True if the player has at least one winning position on the board
    """
    #horizontal stripes
    if board[0][0] == player and board[0][0]==board[0][1] and board[0][1]==board[0][2]:
        return True
    if board[1][0]==player and board[1][0]==board[1][1] and board[1][1]==board[1][2]:
        return True
    if board[2][0]==player and board[2][0]==board[2][1] and board[2][1]==board[2][2]:
        return True

    #vertical stripes
    if board[0][0] == player and board[0][0]==board[1][0] and board[1][0]==board[2][0]:
        return True
    if board[0][1] == player and board[0][1]==board[1][1] and board[1][1]==board[2][1]:
        return True
    if board[0][2] == player and board[0][2]==board[1][2] and board[1][2]==board[2][2]:
        return True
    
    #diagonals
    if board[0][0] == player and board[0][0]==board[1][1] and board[1][1]==board[2][2]:
        return True
    if board[0][2] == player and board[0][2]==board[1][1] and board[1][1]==board[2][0]:
        return True
    
    #no win on the board
    return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #player to be verifyied: X
    if win_condition(board,X):
        return X
    elif win_condition(board,O):
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #game won by someone
    possible_winner = winner(board)
    if possible_winner != None:
        return True
    else:
        #verify if game drawn
        empty_counter = 0
        for line in board:
            for cell in line:
                if cell ==EMPTY:
                    empty_counter+=1
        if empty_counter == 0:#all cells occupyied so its a draw
            return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) ==X:
        return 1
    elif winner(board)==O:
        return -1
    return 0

def max_value(board):
    if terminal(board):
        return utility(board)
    else:
        v =-math.inf
        for act in actions(board):
            v = max(v,min_value(result(board,act)))
        return v
def min_value(board):
    if terminal(board):
        return utility(board)
    else:
        v = math.inf
        for act in actions(board):
            v = min(v,max_value(result(board,act)))
        return v
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    best_action = None
    current = player(board)

    if current == X:
        best_value = -math.inf
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
    else:  # current == O
        best_value = math.inf
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action

    return best_action



