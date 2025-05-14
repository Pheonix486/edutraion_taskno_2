# tic_tac_toe_ai.py

import math

# Create a 3x3 empty board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    print()
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")
    print()

# Check if a player has won
def is_winner(brd, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(all(brd[i] == player for i in cond) for cond in win_conditions)

# Check if the board is full (draw)
def is_draw(brd):
    return " " not in brd

# Minimax algorithm
def minimax(brd, depth, is_maximizing):
    if is_winner(brd, "O"):
        return 1
    elif is_winner(brd, "X"):
        return -1
    elif is_draw(brd):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if brd[i] == " ":
                brd[i] = "O"
                score = minimax(brd, depth + 1, False)
                brd[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if brd[i] == " ":
                brd[i] = "X"
                score = minimax(brd, depth + 1, True)
                brd[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI move using Minimax
def ai_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    print_board()

    while True:
        # Human move
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != " ":
            print("Invalid move. Try again.")
            continue
        board[move] = "X"
        print_board()

        if is_winner(board, "X"):
            print("You win!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        # AI move
        ai_move()
        print("AI played:")
        print_board()

        if is_winner(board, "O"):
            print("AI wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

# Start the game
play_game()

input("\nPress Enter to exit...")  # Prevents auto-closing
