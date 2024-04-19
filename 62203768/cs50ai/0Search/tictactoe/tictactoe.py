"""
Tic Tac Toe Player
"""

import math
import copy

# Global variables to define the players' symbols
X = "X"
O = "O"
# Global variable to define the state of an empty cell
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
    # The player function should take a board state as input, and return which player’s turn it is (either X or O). In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move. Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).

    # Initialize a counter for each player
    x_count = 0
    o_count = 0

    # Count the symbols on the board and increment the counters for each player as required
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X:
                x_count += 1
            if board[row][col] == O:
                o_count += 1

    # If there are more Xs than Os on the board, it is O's turn
    if x_count > o_count:
        return O
    # Or if there are an equal number of them and the game is not over yet, it is X's turn
    elif x_count == o_count and not terminal(board):
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # The actions function should return a set of all of the possible actions that can be taken on a given board.
    # Each action should be represented as a tuple (i, j) where i corresponds to the row of the move (0, 1, or 2) and j corresponds to which cell in the row corresponds to the move (also 0, 1, or 2).
    # Possible moves are any cells on the board that do not already have an X or an O in them.
    # Any return value is acceptable if a terminal board is provided as input.

    # Initialize the empty set to hold all the empty (available) cells
    available = set()

    # Loop through all the cells and add the empty ones to the set
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                available.add((row, col))

    # Return the set of all available cells
    return available


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # The result function takes a board and an action as input, and should return a new board state, without modifying the original board. If action is not a valid action for the board, your program should raise an exception. The returned board state should be the board that would result from taking the original input board, and letting the player whose turn it is make their move at the cell indicated by the input action. Importantly, the original board should be left unmodified: since Minimax will ultimately require considering many different board states during its computation. This means that simply updating a cell in board itself is not a correct implementation of the result function. You’ll likely want to make a deep copy of the board first before making any changes.

    # If the action is not a valid action for the board, raise an exception.
    if action not in actions(board):
        return Exception("Invalid move")
    else:
        # Assign variables for action co-ordinates
        row, col = action
        # Copy the board to a new board
        new_board = copy.deepcopy(board)
        # Add the action co-ordinates to the new board
        new_board[row][col] = player(board)

    return new_board


# Helper function to check rows for the winner function
def check_row(board, player):
    """
    Checks if any player has three in a row
    """
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False


# Helper function to check columns for the winner function
def check_col(board, player):
    """
    Checks if any player has three in a column
    """
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    return False


# Helper function to check down diagonal for the winner function
def check_down_diag(board, player):
    """
    Checks if any player has three in a diagonal going from top left to bottom right
    """
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row == col and board[row][col] == player:
                count += 1
    if count == 3:
        return True
    else:
        return False


# Helper function to check up diagonal for the winner function
def check_up_diag(board, player):
    """
    Checks if any player has three in a diagonal going from bottom left to top right
    """
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (len(board) - (row - 1)) == col and board[row][col] == player:
                count += 1
    if count == 3:
        return True
    else:
        return False


def winner(board):
    """
    Returns the winner of the game if there is one.
    """
    # The winner function should accept a board as input, and return the winner of the board if there is one.
    # If the X player has won the game, your function should return X. If the O player has won the game, your function should return O.
    # One can win the game with three of their moves in a row horizontally, vertically, or diagonally.
    # You may assume that there will be at most one winner (that is, no board will ever have both players with three-in-a-row, since that would be an invalid board state).
    # If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the function should return None.

    # If any of the helper functions returns True, a winner is returned, or else there is no winner
    if (
        check_row(board, X)
        or check_col(board, X)
        or check_down_diag(board, X)
        or check_up_diag(board, X)
    ):
        return X
    elif (
        check_row(board, O)
        or check_col(board, O)
        or check_down_diag(board, O)
        or check_up_diag(board, O)
    ):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # The terminal function should accept a board as input, and return a boolean value indicating whether the game is over. If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, the function should return True. Otherwise, the function should return False if the game is still in progress.

    # If the winner function returns either player, the game is over
    if winner(board) == X or winner(board) == O:
        return True
    # Loop through the board and return False is there are any available cells as the game is not over yet
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return False
    # Otherwise the game is over and there is no winner
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # The utility function should accept a terminal board as input and output the utility of the board. If X has won the game, the utility is 1. If O has won the game, the utility is -1. If the game has ended in a tie, the utility is 0. You may assume utility will only be called on a board if terminal(board) is True.

    # Return 1 if X is the winner, -1 if O is the winner, and 0 if there is no winner
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


# Helper function to get maximum values for the minimax function
def maximum(board):
    """
    Returns the maximum value of all possible actions
    """

    # Sets a variable to a value of minus infinity
    v = -math.inf

    # If the game is over, return a utility value to determine the outcome
    if terminal(board):
        return utility(board)

    # Assign the maximum value attained from comparing the v variable to the result of the minimun function to v
    for action in actions(board):
        v = max(v, minimum(result(board, action)))

    return v


# Helper function to get minimum values for the minimax function
def minimum(board):
    """
    Returns the minimum values of all possible actions
    """

    # Sets a variable to a value of infinity
    v = math.inf

    # If the game is over, return a utility value to determine the outcome
    if terminal(board):
        return utility(board)

    # Assign the minimum value attained from comparing the v variable to the result of the maximum function to v
    for action in actions(board):
        v = min(v, maximum(result(board, action)))

    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # The minimax function should take a board as input, and return the optimal move for the player to move on that board. The move returned should be the optimal action (i, j) that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable. If the board is a terminal board, the minimax function should return None.

    # If the board is a terminal board, the minimax function returns None.
    if terminal(board):
        return None

    # If the current player is X ie. the player trying to maximize
    elif player(board) == X:
        # List to store all of the actual moves
        moves = []
        # Loop over all of the possible actions
        for action in actions(board):
            # Adds the minimum value and the action (move) to get to that value to the moves list
            moves.append([minimum(result(board, action)), action])
        # The return value of the lambda function is reversed and sorted to get the maximum and the required action to achieve that value is returned by accessing the second element of the tuple
        return sorted(moves, key=lambda x: x[0], reverse=True)[0][1]

    # If the current player is O ie. the player trying to minimize
    elif player(board) == O:
        # List to store all of the actual moves
        moves = []
        # Loop over all of the possible actions
        for action in actions(board):
            # Adds the maximum value and the action (move) to get to that value to the moves list
            moves.append([maximum(result(board, action)), action])
        # The return value of the lambda function is sorted to get the minimum and the required action to achieve that value is returned by accessing the second element of the tuple
        return sorted(moves, key=lambda x: x[0])[0][1]
