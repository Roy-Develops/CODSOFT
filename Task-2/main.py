import tkinter as tk
from tkinter import messagebox

# Constants for the game
EMPTY = " "
PLAYER_X = "X"
PLAYER_O = "O"
AI_PLAYER = PLAYER_O  # AI player is "O"

# Create an empty 3x3 board
board = [EMPTY] * 9

# Initialize the GUI
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create buttons for each cell in the 3x3 grid
buttons = []
for i in range(9):
    row = i // 3
    col = i % 3
    button = tk.Button(root, text=EMPTY, font=("Helvetica", 24), width=6, height=2,
                       command=lambda i=i: make_move(i))
    button.grid(row=row, column=col)
    buttons.append(button)


# Function to make a move
def make_move(i):
    if board[i] == EMPTY and not is_game_over(board):
        buttons[i]["text"] = PLAYER_X
        board[i] = PLAYER_X
        if not is_game_over(board):
            ai_move()


# Minimax algorithm
def minimax(board, depth, is_maximizing):
    scores = {
        PLAYER_X: -1,
        PLAYER_O: 1,
        "tie": 0
    }

    result = evaluate(board)

    if result in scores:
        return scores[result]

    if is_maximizing:
        max_eval = float("-inf")
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI_PLAYER
                eval = minimax(board, depth + 1, False)
                board[i] = EMPTY
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_X
                eval = minimax(board, depth + 1, True)
                board[i] = EMPTY
                min_eval = min(min_eval, eval)
        return min_eval


def ai_move():
    best_move = None
    best_eval = float("-inf")
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI_PLAYER
            eval = minimax(board, 0, False)
            board[i] = EMPTY
            if eval > best_eval:
                best_eval = eval
                best_move = i

    if best_move is not None:
        buttons[best_move]["text"] = PLAYER_O
        board[best_move] = PLAYER_O
        if is_game_over(board):
            return

# Function to check for a win, loss, or a tie
def evaluate(board):
    for combo in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != EMPTY:
            return board[combo[0]]
    if EMPTY not in board:
        return "tie"
    return None


# Function to check if the game is over
def is_game_over(board):
    result = evaluate(board)
    if result:
        if result == "tie":
            messagebox.showinfo("Game Over", "The game is a tie!")
        else:
            messagebox.showinfo("Game Over", f"The winner is {result}!")
        root.quit()
        return True
    return False


root.mainloop()
