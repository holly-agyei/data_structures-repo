import random

def init_board():
    """Initialize a 4x4 game board."""
    return [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

def add_random(board):
    """Add a random tile (2 or 4) to the board."""
    empty = [(r, c) for r in range(4) for c in range(4) if board[r][c] == 0]
    if empty:
        r, c = random.choice(empty)
        board[r][c] = random.choice([2, 4])

def compress(board):
    """Compress the board by moving all non-zero tiles to the left."""
    for r in range(4):
        new_row = [x for x in board[r] if x != 0]
        new_row += [0] * (4 - len(new_row))
        board[r] = new_row

def merge(board):
    """Merge adjacent tiles with the same value."""
    for r in range(4):
        for c in range(3):
            if board[r][c] == board[r][c + 1] and board[r][c] != 0:
                board[r][c] *= 2
                board[r][c + 1] = 0

def move_left(board):
    """Move all tiles to the left."""
    compress(board)
    merge(board)
    compress(board)

def move_right(board):
    """Move all tiles to the right."""
    board = [row[::-1] for row in board]
    move_left(board)
    board = [row[::-1] for row in board]

def move_up(board):
    """Move all tiles up."""
    board = list(zip(*board))
    move_left(board)
    board = list(map(list, zip(*board)))

def move_down(board):
    """Move all tiles down."""
    board = list(zip(*board))
    move_right(board)
    board = list(map(list, zip(*board)))

def print_board(board):
    """Print the current state of the board."""
    for row in board:
        print("\t".join(map(str, row)))
    print()

def game_over(board):
    """Check if the game is over."""
    for r in range(4):
        for c in range(3):
            if board[r][c] == 0 or board[r][c] == board[r][c + 1]:
                return False
    for c in range(4):
        for r in range(3):
            if board[r][c] == 0 or board[r][c] == board[r + 1][c]:
                return False
    return True

def play_game():
    """Play the 2048 game."""
    board = init_board()
    add_random(board)
    add_random(board)

    while not game_over(board):
        print_board(board)
        move = input("Move (l/r/u/d): ").lower()
        if move == 'l':
            move_left(board)
        elif move == 'r':
            move_right(board)
        elif move == 'u':
            move_up(board)
        elif move == 'd':
            move_down(board)
        
        add_random(board)
    print("Game Over!")

play_game()