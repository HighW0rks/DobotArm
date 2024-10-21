import sys
from pydobot import Dobot
sys.path.append('../TicTacToe')

import TicTacToeEngine as engine

device = Dobot(port="COM15")
device.speed(100,100)

position_row = [220, 260, 300]
position_col = [-40, 0, 40]
red_pos = [(200, -80), (200, -120), (200, -160), (240,-80), (240, -120)]
yellow_pos = [(200,80), (200, 120), (200, 160), (240, 80), (240, 120)]
turn_red = 0
turn_yellow = 0

def move(x, y, z, suck):
    device.move_to(x=x, y=y, z=z, r=0, wait=True)
    device.suck(suck)

def doBotClearBoard():
    global turn_yellow
    global turn_red
    #print("Clear")
    turn_yellow = 0
    turn_red = 0

def doBotMove(piece, pos):
    global turn_red
    global turn_yellow
    if piece == "X":
        pos_piece = yellow_pos[turn_yellow]
        move(pos_piece[0], pos_piece[1], -10, False)
        move(pos_piece[0], pos_piece[1], -50, True)
        move(pos_piece[0], pos_piece[1], -10, True)
        move(position_row[pos[1]], position_col[pos[0]], -10, True)
        move(position_row[pos[1]], position_col[pos[0]], -50, False)
        move(position_row[pos[1]], position_col[pos[0]], -10, False)
        turn_yellow += 1

    if piece == "O":
        pos_piece = red_pos[turn_red]
        move(pos_piece[0], pos_piece[1], -10, False)
        move(pos_piece[0], pos_piece[1], -50, True)
        move(pos_piece[0], pos_piece[1], -10, True)
        move(position_row[pos[1]], position_col[pos[0]], -10, True)
        move(position_row[pos[1]], position_col[pos[0]], -50, False)
        move(position_row[pos[1]], position_col[pos[0]], -10, False)
        turn_red += 1

"""
    piece is last piece
    pos is position of last piece
"""
def showBoard(board, piece, pos):
    doBotMove(piece, pos)
    field = "-" * 13 + "\n"
    for row in board:
        field += "|"
        for piece in row:
            if piece is None:
                field += "{:3}|".format('')
            else:
                field += "{:^3}|".format(piece)
        field += "\n" + "-" * 13 + "\n"
    print(field)
    
def inputKey(text, allowedKeys):
    while True:
        key = input(text)
        if key in allowedKeys:
            return key

def getBestPosition(board, piece, other):
    pos = engine.getBestPosition(board, piece, other)
    
    return pos

"""
"""    

def getCoordinate(board, piece, other):
    while True:
        position = input(f"Geef de coordinaten van je stuk [{piece}] in x,y :")
        position = position.split(',')
        if len(position) != 2:
            continue
        try:
            x = int(position[0])
            y = int(position[1])
            if engine.isPositionEmpty(board, x, y):
                return x, y
        except:
            print("No valid coordinate")
            continue


def game(boardOutput, inputPlayer1, inputPLayer2):
    print("")
    print("+++++++++++++")
    print("- NEW  GAME +")
    print("+++++++++++++")
    print("")
    hasWinner = engine.game(boardOutput, inputPlayer1, inputPLayer2)
    if hasWinner:
        print("The winner is : ", hasWinner)
    return hasWinner

def start():
    inputPlayer1 = getBestPosition #getCoordinate
    inputPlayer2 = getBestPosition
        
    hasWinner = False
    while not hasWinner:
        doBotClearBoard()
        hasWinner = game(showBoard, inputPlayer1, inputPlayer2)

"""
                         _____ _____ ____ _____      __  ____  _____ __  __  ___  
                        |_   _| ____/ ___|_   _|    / / |  _ \| ____|  \/  |/ _ \ 
                          | | |  _| \___ \ | |     / /  | | | |  _| | |\/| | | | |
                          | | | |___ ___) || |    / /   | |_| | |___| |  | | |_| |
                          |_| |_____|____/ |_|   /_/    |____/|_____|_|  |_|\___/ 
"""

if __name__ == "__main__":
    start()