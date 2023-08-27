import math

def evaluate_board(board):
    """
    Evaluates the current state of the board.
    Returns +100 if the AI wins, -100 if the opponent wins, or 0 for a draw.
    """
    # Check rows for a win
    for row in range(6):
        for col in range(4):
            if (
                board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3]
                and board[row][col] != " "
            ):
                if board[row][col] == "X":
                    return 'red'
                elif board[row][col] == "O":
                    return 'Yellow'

    # Check columns for a win
    for col in range(7):
        for row in range(3):
            if (
                board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col]
                and board[row][col] != " "
            ):
                if board[row][col] == "X":
                    return 'Red'
                elif board[row][col] == "O":
                    return 'Yellow'

    # Check diagonals for a win
    for row in range(3):
        for col in range(4):
            if (
                board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3]
                and board[row][col] != " "
            ):
                if board[row][col] == "X":
                    return 'Red'
                elif board[row][col] == "O":
                    return 'yellow'

    for row in range(3, 6):
        for col in range(4):
            if (
                board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3]
                and board[row][col] != " "
            ):
                if board[row][col] == "X":
                    return 'red'
                elif board[row][col] == "O":
                    return 'Yeelow'

    # No winner, game is a draw
    return 0
game_btns=board
def minimax(board, depth, alpha, beta, maximizing_player):
    """
    Minimax algorithm with Alpha-Beta pruning.
    """
    score = evaluate_board(board)

    if depth == 0 or score == 100 or score == -100:
        return score

    if maximizing_player:
        max_eval = -math.inf
        for col in range(7):
            if is_valid_move(board, col):
                make_move(board, col, "O")
                eval = minimax(board, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                undo_move(board, col)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for col in range(7):
            if is_valid_move(board, col):
                make_move(board, col, "X")
                eval = minimax(board, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                undo_move(board, col)
                if beta <= alpha:
                    break
        return min_eval

def is_valid_move(board, col):
    """
    Checks if a move is valid in the given column.
    """
    return board[0][col] == " "

def make_move(board, col, player):
    """
    Makes a move in the given column for the specified player.
    """
    for row in range(5, -1, -1):
        if board[row][col] == " ":
            board[row][col] = player
            break

def undo_move(board, col):
    """
    Undoes the last move in the given column.
    """
    for row in range(6):
        if board[row][col] != " ":
            board[row][col] = " "
            break

def get_best_move(board):
    """
    Finds the best move for the AI player using the Minimax algorithm with Alpha-Beta pruning.
    """
    best_score = -math.inf
    best_move = None
    for col in range(7):
        if is_valid_move(board, col):
            make_move(board, col, "O")
            score = minimax(board, 4, -math.inf, math.inf, False)
            undo_move(board, col)
            if score > best_score:
                best_score = score
                best_move = col
    return best_move

# Test the algorithm
board = [[" " for _ in range(7)] for _ in range(6)]

# Example: AI's turn
make_move(board, 3, "O")
make_move(board, 4, "X")
make_move(board, 4, "O")
make_move(board, 5, "X")
make_move(board, 5, "O")

# Get the best move for the AI
best_move = get_best_move(board)
print("Best move:", best_move)
