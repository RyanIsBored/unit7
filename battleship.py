#Ryan Jones
#5/23/18

def printBoard(board1,board2):
    for r in range(0,5):
        for c in range(0,5):
            print(board1[r][c],end=' ')
        print()

def createBoard():
     return [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]



if __name__ == '__main__':
    player = createBoard()
    computer = createBoard()
    printBoard(player,computer)
    
    row = int(input('Enter a row: '))
    col = int(input('Enter a column: '))
    player[row-1][col-1] = 'X'
    printBoard(player,computer)