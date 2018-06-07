#Ryan Jones
#5/23/18
from random import randint
def printBoard(board1,board2):
    for r in range(0,5):
        for c in range(0,5):
            print(board1[r][c],end=' ')
        print()
    print(' ')
    for r in range(0,5):
        for c in range(0,5):
            print(board2[r][c],end=' ')
        print()

def createBoard():
     return [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

def placePlayerShips(player):
    ship1 = input("Where do you want to place your first ship?: ")
    [row,col]=getIndices(ship1)
    player[row][col] = 'X'
    ship2 = input("Where do you want to place your second ship?: ")
    [row,col]=getIndices(ship2)
    player[row][col] = 'X'
    ship3 = input("Where do you want to place your third ship?: ")
    [row,col]=getIndices(ship3)
    player[row][col] = 'X'

def placeComputerShips(computer):
    [row]=randint(0,4)
    [col]=randint(0,4)
    ship4[row][col] = 'X'
    

def getIndices(coord):
    if coord[0]=='A':
        row=0
    if coord[0]=='B':
        row=1
    if coord[0]=='C':
        row=2
    if coord[0]=='D':
        row=3
    if coord[0]=='E':
        row=4
    col=int(coord[1])-1
    return[row,col]

if __name__ == '__main__':
    player = createBoard()
    computer = createBoard()
    printBoard(player,computer)
    
    placePlayerShips(player)
    placeComputerShips(computer)
    printBoard(player,computer)