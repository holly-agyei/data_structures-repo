"""
import random

def init_board():
    return [[0,0,0,0] for _ in range(4)]

def add_random(board):
    empty = []
    for r in range(4):
        for c in range(4):
            if board[r][c] == 0:
              empty.append((r,c))
    
    if empty:
    
      r,c = random.choice(empty)
      board[r][c] = random.choice([2,4])

#print
def print_board(board):
    for row in board:
      print("\t".join(map(str, row)))
    print()
    
def move_left(board):
    for r in range(4):
      compress(board[r])
      merge(board[r])
      compress(board[r])
      
def compress(row):
    new_row = [x for x in row if x!=0]
    new_row += [0]*(4-len(new_row))
    for i in range(4):
        row[i] = new_row[i]
        
def merge(row):
    for i in range(3):
        if row[i] == row[i+1] and row[i] != 0:
            row[i] *=2 
            row[i+1] = 0

def move_up(board):
    #extract each colum
    for c in range(4):
        column  = [board[r][c] for r in range(4)]
        compress(column)
        merge(column)
        compress(column)
        
        for r in range(4):
            board[r][c] = column[r]
            
def move_down(board):
    for c in range(4):
        column = [board[r][c] for r in range(4)]
        column.reverse()
        compress(column)
        merge(column)
        compress(column)
        column.reverse()
        
        for r in range(4):
            board[r][c] = column[r]
def move_right(board):
    for r in range(4):
        row = board[r][::-1]
        compress(row)
        merge(row)
        compress(row)
        
        board[r] = row[::-1]
        
#cehck for game over:
def check_gameover(board):
    for r in range(4):
        for c in range(4):
            if board[r][c] == 0:
                return False
            if c<3 and board[r][c] == board[r][c+1]:
                return False
            if r< 3 and board[r][c] == board[r+1][c]:
                return False
    return True
    

def check_win(board):
    for rows in board:
        if 2048 in rows:
            return True
    return False

def play_game():
    board = init_board()
    add_random(board)
    add_random(board)
    
    while not check_gameover(board):
        print_board(board)
        
        move = input("where do you want to move ")
        if move == "l":
            move_left(board)
        elif move == "r":
            move_right(board)
        elif move =="d":
            move_down(board)
        elif move == "u":
            move_up(board)
        else: 
            print("enter a valied option")
            continue
        #after choosing an option, a random number is added
        add_random(board)
        
        if check_win(board):
            print("won")
            break #break the game
        

    print("grame over")


        
play_game()

    

"""

def solution(logs):
    item_price = {}
    revenue = []
    for log in logs:
        if log[0] == "sell":
            count = int(log[2])
            curr_rev = 0
            while count:
                curr_rev += item_price.get(log[1]).pop()
                count -= 1
            revenue.append(curr_rev)
        elif log[0] == "supply":
            count = int(log[2])
            
            while count:
                item_price[log[1]] = item_price.get(log[1], []) + [int(log[3])]
                count -= 1
        else:
            count = int(log[2])
            
            while count:
                item_price[log[1]] = item_price.get(log[1], []) + [int(log[4])]
                count -= 1
                
    return revenue











