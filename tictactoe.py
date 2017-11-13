
class FieldState:
    PLAYERX = -1
    FREE = 0
    PLAYERO = 1

class Field:
    
    def __init__(self, row, column):
        self._state = FieldState.FREE
        self._row = row
        self._column = column

    def take(self, player):
        self._state = player

class Board:
    
    def __init__(self, dimension):
        self._fields = {(row, column): Field(row, column)
                       for row in range(dimension)
                       for column in range(dimension)}


class Tictactoe:
    
    def __init__(self, boardDimsension):
        self.n = boardDimsension
        self.board = self.createBoard()
        self.moveCount = 0

    def createBoard(self):
        return [['.' for row in range(self.n)] for col in range(self.n)]

    def spotTaken(self, row, col):
        if self.board[row][col] != '.': return True
        else: return False

    def playTurn(self, row, col, player):
        self.moveCount += 1
        if not self.spotTaken(row, col):
          self.board[row][col] = player
          self.checkWin(row, col, player)
        else:
            return

    def printBoard(self):
        print('-' * (self.n * 2 + 1))
        for row in range(self.n):
            for column in range(self.n):
                print('|' + self.board[row][column], end='')
            if column == self.n - 1:
                print('|')
            else:   
                print('|\n')
        print('-' * (self.n * 2 + 1))

    def checkWin(self, row, col, player):

        #check row
        for i in range(self.n):
            if self.board[row][i] != player:
                break
            if i == self.n-1:
                print("Row! Player " + player + ' have won!')

        #check column
        for i in range(self.n):
            if self.board[i][col] != player:
                break
            if i == self.n-1:
                print("Column! Player " + player + ' have won!')

        #check diag
        if row == col:
            #we're on a diagonal
            for i in range(self.n):
                if self.board[i][i] != player:
                    break
                if i == self.n-1:
                    print("Diag! Player " + player + ' have won!')
        #check anti diag 
        if col + row == self.n - 1:
            for i in range(self.n):
                if self.board[i][(self.n-1)-i] != player:    
                    break
                if i == self.n-1:
                    print("Player " + player + ' have won!')

        #check draw
        if self.moveCount == self.n**2:
            print("It's a tie!")


game = Tictactoe(3)
game.printBoard()
game.playTurn(0, 1, 'X')
game.playTurn(1, 1, 'X')

game.playTurn(1, 0, 'X')
game.playTurn(0, 2, 'O')
game.playTurn(2, 0, 'X')
game.playTurn(0, 0, 'O')
game.playTurn(1, 2, 'O')
game.playTurn(2, 2, 'X')
game.playTurn(2, 1, 'O')
game.printBoard()
#print(game.checkwin(game.board)
board = Board(3)
print(board._fields[1,2]._state)
board._fields[1,2].take(FieldState.PLAYERX)
print(board._fields[1,2]._state)