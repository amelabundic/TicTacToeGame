"""
Tic Tac Toe Player
"""

import copy
import math

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
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    
    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set() 

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    
    return possible_actions  


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)

    current_player = player(board)

    if new_board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid action")

    new_board[action[0]][action[1]] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0] 
        
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != EMPTY:
            return board[0][j] 

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0] 
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2] 

    return None 


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True

    for row in board:
        if EMPTY in row: 
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0 


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        best_value = -math.inf
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            move_value = minimax_value(new_board)
            if move_value > best_value:
                best_value = move_value
                best_action = action
        return best_action

    else:  
        best_value = math.inf
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            move_value = minimax_value(new_board)
            if move_value < best_value:
                best_value = move_value
                best_action = action
        return best_action

def minimax_value(board):
    """
    Returns the value of the board for the current player.
    """
    if terminal(board):
        return utility(board)

    if player(board) == X:
        best_value = -math.inf
        for action in actions(board):
            new_board = result(board, action)
            best_value = max(best_value, minimax_value(new_board))
        return best_value 

    else:
        best_value = math.inf
        for action in actions(board):
            new_board = result(board, action)
            best_value = min(best_value, minimax_value(new_board))
        return best_value
