import random
from time import sleep
POSITION_TO_ACTION = { (0,3): "NEW", (0,4) : "AUTO" }
ACTION_TO_POSITION = { "NEW" : (0,3),  "AUTO": (0,4) }
SLEEP_BETWEEN_MOVES = 0.3
"""
    Tic Tac Toe
    Er is een manier om te winnen tegen de computer :)
"""

PIECES = ("X", "O")

"""
    Return a matrix of a board with the dimensions of size x size
    e,g, size = 3
    returns : [ [None, None, None], [None, None, None], [None, None, None] ]
    The board is a list of lists. board= [ [00, 01, 02], [10, 11, 12], [20, 21, 22] ]
        00  01  02
        10  11  12
        20  21  22
    board[1][0] = 10
    board[2][1] = 21
    
    x[y][x] 
"""
def getEmptyBoard(size = 3):
    return [[None]*size for i in range(size)]

"""
    Is the given position with posX and posY empy on the board (value is None)
"""
def isPositionEmpty(board, posX, posY):
    return getPiece(board, posX, posY) == None

"""
    Get a dictionary of all occupied fields per piece
"""
def getOccupied(board):
    locations = {}
    size = len(board)
    posY = 0
    while posY < size:
        posX = 0
        while posX < size:
            piece = getPiece(board, posX, posY)
            if piece != None:
                if piece in locations:
                    locations[piece].append((posX, posY))
                else:
                    locations[piece] = [(posX, posY)]
            posX += 1
        posY += 1
    return locations;
    
"""
    Get the piece at the positon [posX], [posY] on the given [board]
"""
def getPiece(board, posX, posY):
    size = len(board)
    if posX < 0 or posX >= size: #controleer of de [posX] binnen de grenzen ligt
        raise Exception('Location not valid')
    if posY < 0 or posY >= size: #controleer of de [posY] binnen de grenzen ligt
        raise Exception('Location not valid')
    return board[posY][posX]

"""
    Set a [piece] on the positon [posX], [posY] on the given [board]
"""
def setPiece(board, posX, posY, piece, force = False):
    if not force and not isPositionEmpty(board, posX, posY):
        return False
    board[posY][posX] = piece
    return True

"""
   Set a [piece] on the positon [pos] on the given [board]
   pos = (x,y)
"""
def setPiecePos(board, pos, piece):
    if pos == None or piece == None:
        return False
    return setPiece(board, pos[0], pos[1], piece)
    
"""
    returns the number of empty positions left on the [board]
"""
def getNumberEmptyPositions(board):
    count = 0
    for y in board:
        for x in y:
            if x == None:
                count += 1
    return count

"""
    returns if there is a winning position on the board (boad is 3x3)
"""
def hasWinner(board):
    size = len(board[0])
    # check if there is a winner on the horizontels
    for y in board:
        first = y[0]
        if first != None:
            for x in y:
                if first != x:
                    break
            else:
                return first
            
    #Check if there us a winner on the verticals
    #[ [1, 0, 0], [1, N, N], [1, 0, 0]]
    for x in range(0, size):
        first = board[0][x]
        if first == None:
            continue
        for y in range(1, size):
            if first != board[y][x]:
                break
        else:
            return first
        
    #check for diagonal left-right
    first = board[0][0]
    if first != None:
        for x in range(1, size):
            if first != board[x][x]:
                break
        else:
            return first
    
    #check for diagonal right-left
    first = board[0][size-1]
    if first != None:
        y = 0
        x = size-1
        for i in range(1, size):
            if first != board[y + i][x - i]:
                break
        else:
            return first
            
    return None

"""
    set [piece] on every position that has None at this moment on the [board]
    and check if this situation is a winning move
"""
def getWinningMove(board, piece):
    size = len(board)
    for y in range(size):
        for x in range(size):
            if not isPositionEmpty(board, x, y): 
                continue # if there is a piece on the location, continue
            if setPiece(board, x, y, piece):  # set a piece on the None location
                winner = hasWinner(board)
                setPiece(board, x, y, None, True)   # Return the origional situation
                if winner == piece:
                    return x,y
    return None

def shuffle(lst):
    moves = []
    while len(lst) != 0:
        moves.append(lst.pop(random.randint(0, len(lst)-1)))
    return moves

"""
    board with dimensions 3x3
    piece is your own piece
    other is piece of other party
"""
def getBestPosition(board, piece, other):
    sleep(SLEEP_BETWEEN_MOVES)
    
    #if empty -> (random.randint(0, 2), random.randint(0, 2))

    # Is het midden beschikbaar, is een hoek beschikbaar, is een zijkant beschikbaar
    BEST_MOVES = [(0,0),(2,2),(2,0),(0,2),(0,1),(1,0),(1,2),(2,1)]

    # is er een plek die winst geeft?
    pos = getWinningMove(board, piece)
    if pos != None:
        return pos
    
    # other has clear winner
    pos = getWinningMove(board, other)
    if pos != None:
        return pos
    
    # Is het midden beschikbaar
    if board[1][1] == None:
        return (1,1)
    
    moves = shuffle(BEST_MOVES)
    
    for y,x in moves:
        if board[y][x] == None:
            return (x,y)
    return None

"""
    boardOutput is a function that shows the board
    with one parameter the board matrix
    
    boardOutput(board)
    getCoordinate(board, piece)
"""
def game(boardOutput, inputPlayer1, inputPlayer2):
    ttt = TicTacToeEngine()
    #boardOutput(ttt.getBoard(), None, None)
    while not ttt.gameFinished():
        board = ttt.getBoard()
        if ttt.isPlayer1():
            best = inputPlayer1(board, ttt.other, ttt.piece)
        else:
            best = inputPlayer2(board, ttt.piece, ttt.other)
        if ttt.inputCurrentPlayer(best):
            boardOutput(board, ttt.other, best)
            
    return ttt.hasWinner()

class TicTacToeEngine():
    def __init__(self):        
        self.board = getEmptyBoard()
        self.move = 0
        self.player1 = random.randint(1, 1000) % 2 == 0
        self._currentPlayer()
    
    
    def getBoard(self):
        return self.board
    
    def isPlayer1(self):
        return self.player1
    
    def getPieces(self):
        return self.piece, self.other
    
    def gameFinished(self):
        return self.hasWinner() or 0 == getNumberEmptyPositions(self.board)
    
    def hasWinner(self):
        return hasWinner(self.board)
    
    def _currentPlayer(self):
        self.piece = PIECES[self.move % 2]
        self.other = PIECES[(1 + self.move) % 2]
    
    def inputCurrentPlayer(self, best):        
        if setPiecePos(self.board, best, self.piece):
            self.move += 1
            self.player1 = not self.player1
            self._currentPlayer()
            
#             if not hasWinner(self.board) and self.player1 == False and self.autoPlayer2 == True:
#                 best = getBestPosition(self.board, self.piece, self.other)
#                 self.inputCurrentPlayer(best)
            return True
        return False
    
"""
                         _____ _____ ____ _____      __  ____  _____ __  __  ___  
                        |_   _| ____/ ___|_   _|    / / |  _ \| ____|  \/  |/ _ \ 
                          | | |  _| \___ \ | |     / /  | | | |  _| | |\/| | | | |
                          | | | |___ ___) || |    / /   | |_| | |___| |  | | |_| |
                          |_| |_____|____/ |_|   /_/    |____/|_____|_|  |_|\___/ 
"""
if __name__ == "__main__":
    print("Start testing")
    try:
        assert(getPiece ([[1, 0, 1], [1, None, 0], [1, None, None]], -1, 0) == 0 )
        assert(False)
    except:
        assert(True) # raise Exception('Location not valid') was executed because -1 is not valid
        
    assert(getPiece ([[1, 0, 1], [1, None, 0], [1, None, None]], 1, 0) == 0 ) 
    assert(hasWinner([[1, 0, 1], [1, None, 0], [1, None, None]]) == 1), "Vertical winner 0"
    assert(hasWinner([[1, 0, 1], [None, 0, None], [None, 0, None]]) == 0), "Vertical winner 1"
    assert(hasWinner([[1, 0, 1], [None, None, 1], [None, 0, 1]]) == 1), "Vertical winner 2"
   
    assert(hasWinner([[1, 1, 1], [None, None, None], [None, None, None]]) == 1), "Horizontal winner 0"
    assert(hasWinner([[None, None, None], [1, 1, 1], [None, None, None]]) == 1), "Horizontal winner 1"
    assert(hasWinner([[None, None, None], [None, None, None], [1, 1, 1]]) == 1), "Horizontal winner 2"
     
    assert(hasWinner([[1, 0, 0], [0, 1, None], [0, None, 1]]) == 1), "Diagonal winner"
    assert(hasWinner([[1, 1, 0], [0, 0, None], [0, 1, None]]) == 0), "Diagonal winner"
     
    assert(hasWinner([[1, 0, 1], [0, None, None], [1, 0, None]]) == None), "No winner"

    assert(getWinningMove([[None, None, None], [1, None, 1], [None, None, None]], 1) == (1,1))
    assert(getWinningMove([[0, None, 1], [1, 0, 1], [None, None, None]], 1) == (2,2))
    assert(getWinningMove([[1, None, 1], [None, None, None], [None, None, None]], 1) == (1,0))
    
    assert(getBestPosition([[None, None, None], [None, 1, None], [None, 1, None]], 1, 0) == (1,0)), "Best position is to win (0,1)"
    assert(getBestPosition([[None, None, None], [None, 0, None], [None, None, 0]], 1, 0) == (0,0)),  "Best position is to win (0,0)"
    assert(getBestPosition([[0, None, 0], [None, None, None], [None, None, None]], 0, 1) == (1,0)), "Best position is to win (0,1)"
   
    assert(getNumberEmptyPositions([[0, None, 0], [1, 0, 1], [None, 1, None]]) == 3), "Three empty positions left"
    print("All tests OK")