#TicTacToe
def display_board(board):
    
    print (board[0] + " | " + board[1] + " | " + board[2])
    print ("-" + " - " + "-" + " - " +    "-")
    print (board[3] + " | " + board[4] + " | " + board[5])
    print ("-" + " - " + "-" + " - " +    "-")
    print (board[6] + " | " + board[7] + " | " + board[8])
def turn(pos,player,Board):
    if player=='X':
        Board[pos]= 'X'
        display_board(Board)
    if player == 'O':
        Board[pos]= 'O'
        display_board(Board)
def checkWin(board,player,win):
    if board[0]==board[1]==board[2]== player:       
            win=True
    elif board[0]==board[1]==board[2]== player:       
            win=True
    elif board[0]==board[1]==board[2]== player:       
            win=True
    elif board[0]==board[1]==board[2]== player:       
            win=True
    elif board[0]==board[1]==board[2]== player:       
            win=True
    elif board[0]==board[1]==board[2]== player:       
            win=True
    elif board[0]==board[1]==board[2]== player:       
            win=True
    elif board[0]==board[1]==board[2]== player:       
            win=True
    return win
    
player1win=False
player2win=False
player1=input("Player 1: Choose X or O\n")
player2=input("Player 2: Choose X or O\n")
win = False
testBoard = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
display_board(testBoard)

while win==False:
    position = int(input("Player 1, Choose a position: "))   
    turn(position,player1.upper(),testBoard)
    player1win=checkWin(testBoard,player1.upper(),win)
    if player1win==True:
        win=True
        continue
    
    position = int(input("Player 2, Choose a position: "))   
    turn(position,player2.upper(),testBoard)
    player2win=checkWin(testBoard,player2.upper(),win)
    if player2win==True:
        win=True
        continue
    
if player1win==True:
    print("Winner: Player 1")
if player2win==True:
    print("Winner: Player 2")
    
    