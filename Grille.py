from math import *
from random import sample
class Grille:

    def __init__(self, taille=9):

        self.size = taille
        self.base = int(sqrt(taille))
        self.side = taille

        rBase = range(self.base)
        rows = [g * self.base + r for g in self.shuffle(rBase) for r in self.shuffle(rBase)]
        cols = [g * self.base + c for g in self.shuffle(rBase) for c in self.shuffle(rBase)]
        nums = self.shuffle(range(1, self.base * self.base + 1))

        # produce board using randomized baseline pattern
        self.boardComplete = [[nums[self.pattern(r, c)] for c in cols] for r in rows]
        for i in range(self.size):
            print(self.boardComplete[i])

    def getGrille(self):
        gridIncomplete = []
        for r in range(self.size):
            row =[]
            for c in range(self.size):
               row.append(self.boardComplete[r][c])
            gridIncomplete.append(row)
        squares = self.side * self.side
        empties = squares * 1 // 2

        for p in sample(range(squares), empties):
            gridIncomplete[p // self.side][p % self.side] = 0

        return gridIncomplete

    def getCompleteGrille(self):
        return self.boardComplete

    def pattern(self, row, col):
        return (self.base*(row%self.base)+row//self.base+col)%(self.side)

    # randomize rows, columns and numbers (of valid base pattern)
    from random import sample
    def shuffle(self, s):
        return sample(s, len(s))

    def getValeur(self, row, column):
        print(self.matrix[row][column])

    def setValeur(self, value, shown, row, column):
        if shown == False:
            value = -value
        self.matrix[row][column] = value

    def afficher(self):

        print("Grille imcomplete\n")
        for i in range(self.size):
            print(self.boardIncomplete[i])

        print("\n Complete")
        for i in range(self.size):
            print(self.boardComplete[i])

    def setGrid(self, grid):
        self.boardComplete = grid[0]
        self.board = grid

    """def testGrille(self, row=0, column=0, value=0):
        completed = True;
        #verified = self.ValueInBlock(row, column, value)
        verified = True
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] <= 0:
                    completed = False;
                if self.matrix[i][j] == value:
                    if i == row or j == column:
                        verified = False
                        print("Le nombre", value, "existe deja en", i, j, )
                        break;

        return verified, completed

    def getBlock(self, row, column):
        if (row == 0 or row == 3 or row == 6):
            xValues = row, row + 2
        elif row == 1 or row == 4 or row == 7:
            xValues = row - 1, row + 1
        else:
            xValues = row - 2, row

        if (column == 0 or column == 3 or column == 6):
            yValues = column, column + 2
        elif column == 1 or column == 4 or column == 7:
            yValues = column - 1, column + 1
        else:
            yValues = column - 2, column

        return (xValues, yValues)

    def ValueInBlock(self, row, column, value):
        unique = True;
        x, y = self.getBlock(row, column)
        for i in range(x[0] - 1, x[1] + 1):
            for j in range(y[0] - 1, y[1] + 1):
                if self.matrix[i][j] == value:
                    unique = False;
                    print("Le nombre", value, "existe deja dans le bloc en", i, j, )
                    break;
        return unique;"""

    """def estRemplie(self):
        completed = True;
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] <= 0:
                    completed = False;

        return completed"""