from IPython.display import clear_output
startcheck = True #To start the game, will be reset by game_end() or full_check() and set by replay()
recheck = False # To check for replay function
position = 0 # Variable for player to input the board position, modified in player_input()
win = False

def setdefault():
    global startcheck
    global recheck
    global position
    global win
    startcheck = True 
    recheck = False 
    position = 0 
    win = False

board = None # List holiding the values of the board
player1 = None # Player 1 character 
player2 = None # Player 2 character

def display_board():
    print(f'\n{board[0]} | {board[1]} | {board[2]}\n---------\n{board[3]} | {board[4]} | {board[5]}\n---------\n{board[6]} | {board[7]} | {board[8]}\n\n')
print("Welcome to Tic Tac Toe\nRules:\n1st player can choose X or O (Use lowercase), Both the players must play turn by turn\nInput the number on the display board to choose the position\nThe player to get 3 X's or O's in a straight line wins\nGood luck :)")

def game_start():
    global board
    global player1
    global player2
    global startcheck
    board = list(range(1,10))
    while True:
        player1 = str(input("Player 1's turn\nChoose X or O\n"))
        if player1 != 'x' and player1 != 'o':
            continue
        elif player1 == 'x':
            player2 = 'o'
            break
        elif player1 == 'o':
            player2 = 'x'
            break
    player1 = player1.upper()
    player2 = player2.upper()
    startcheck = False
    display_board()

def player_input():
    while True:
        global position
        position = int(input('Enter the position: '))
        if position > 9 or position < 1:
            print('Error: Number should be between 1 and 9')
            continue
        elif board[position-1] == 'X' or board[position-1] == 'O':
            print('The position is already filled, please choose an empty slot on the board')
            continue
        else:
            break
    return position

def full_check(inputlist):
    state = 0
    for item in inputlist:
        if item in list(range(1,10)):
            state = 1
    if state == 1:
        return False
    else: 
        print('Draw')
        return True

def win_check(inputlist):
    checklist = [inputlist[0:3],inputlist[3:6],inputlist[6:9],inputlist[0:7:3],inputlist[1:8:3],inputlist[2:9:3],inputlist[0:9:4],inputlist[2:7:2]]
    for item in checklist:
        if item == ['X','X','X']:
            if player1 == 'X':
                print('Player 1 wins')
                return True
            elif player2 == 'X':
                print('Player 2 wins')
                return True
        if item == ['O','O','O']:
            if player1 == 'O':
                print('Player 1 wins')
                return True
            elif player2 == 'O':
                print('Player 2 wins')
                return True

def replay():
    var = str(input('Do you want to play again ? Enter Y to continue'))
    if var == 'Y' or var == 'y':
        clear_output()
        setdefault()
    else:
        print('Thank you for playing\n')
        exit(0)

while True:
    if startcheck == True:
        game_start()
    print("Player 1\n")
    player1in = player_input()
    board[player1in-1] = player1
    clear_output()
    display_board()
    win = win_check(board)
    if not win:
        recheck = full_check(board)
    if recheck or win:
        replay()
        continue
    print("Player 2\n")
    player2in = player_input()
    board[player2in-1] = player2
    clear_output()
    display_board()
    win = win_check(board)
    if not win:
        recheck = full_check(board)
    if recheck or win:
        replay()
