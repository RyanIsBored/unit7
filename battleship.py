#Ryan Jones
#5/23/18

def printBoard(board):
    for r in range(0,5):
        for c in range(0,5):
            print(board[r][c],end=' ')
        print()

board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
printBoard(board)

row = int(input('Enter a row: '))
col = int(input('Enter a column: '))
board[row-1][col-1] = 'X'
printBoard(board)