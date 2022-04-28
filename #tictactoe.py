#tic tac toe
"""
This code is a school asignment to create a step by step code to make a tic tac toe game board
The game is played on a grid that is three squares by three squares.
[
    [-, -, -],
    [-, -, -],
    [-, -, -]

];
Player1_input uses X`s in 1-9
Player2_input uses o`s in 1-0
Players take turns putting their marks in empty squares.
The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner
If they enter anything else: tell them to go again
check if the player_input is already taken
add it to the board
check if user won: checking rows, columns and diagonals
toggle between users upon succesful moves
If all nine squares are full and neither player has three in a row, the game ends in a draw
this program has been developed by Pablo R Sierra (online tutoring and blogs had been used to help get the best outcome for this project) a student of IT technology at BYUI online.

"""
from pickle import FALSE
from sqlite3 import Row


board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]

]

user = True # when true it refers to x, otherwise o
turns = 0

def main(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()    



main(board)           

def quit(player_input):
    if player_input == "q":
        print("Thanks for playing")
        return True 
    else: return False


def check_input(player_input):
    # check if its a number
    if not isnum(player_input): return False
    player_input = int(player_input)
    # check if its 1 - 9
    if not bounds(player_input): return False

    return True

def isnum(player_input):
    if not player_input.isnumeric():
        print("This is not a valid number")
        return False
    else: return True    

def bounds(player_input):
    player_input = int(player_input)    
    if player_input > 9 or player_input < 1:
        print("This number is out of boundry")
        return False
    else: return True    


def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board [row] [col] != "_":
        print("This position is already taken.")
        return True
    else: return False


def coordinates(player_input):
    row = int(player_input /3)
    col = player_input
    if col > 2: col = int(col % 3) 
    return (row, col)


def add_to_board(coords, board, active_user):
    row = coords[0]
    col = coords[1]
    board[row] [col] = active_user

def current_user(user):
    if user: return "x"
    else: return "o"

def iswin(user, board):
    if check_row(user, board): return True
    if check_col(user, board): return True
    if check_diag(user, board): return True
    return False

def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot !=user:
                complete_row = False
                break
        if complete_row: return True
    return False    


def check_col(user, board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row] [col] != user:
                complete_col = False
                break
        if complete_col: return True
    return False        


def check_diag(user, board):
    #top left to bottom right
    if board[0] [0] == user and board[1] [1] == user and board[2] [2] == user: return True
    elif board[0] [2] == user and board[1] [1] == user and board[2] [0] == user: return True
    else: return False


while  turns < 9:
    active_user = current_user(user)
    main(board) 
    player_input = input("Please enter a position 1 through 9 or enter \"q\"to quit:")
    if quit(player_input): break
    if not check_input(player_input):
        print("Please try again.")
        continue
    player_input = int(player_input) -1
    coords = coordinates(player_input)
    if istaken(coords, board):
        print("Please try again.")
        continue
    add_to_board(coords, board, active_user)
    if iswin(active_user, board):
        print(f"{active_user.upper()} won!")
        break 

    turns += 1
    if turns ==9: print("Tie!")




    user = not user