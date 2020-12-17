class Grille:
    matrix = []

    def __init__(self, taille=9):

        self.size = taille

        # Taille de 9 pour verif par bloc
        for i in range(taille):
            row = []
            for j in range(taille):
                row.append(0)
            self.matrix.append(row)
            print(row)

    def getGrille(self):
        return self.matrix

    def getValeur(self, row, column):
        print(self.matrix[row][column])

    def setValeur(self, value, shown, row, column):
        row = row - 1
        column = column - 1
        if shown == False:
            value = -value
        verified, completed = self.testGrille(row, column, value)
        if verified:
            self.matrix[row][column] = value
        # self.afficher()

    def afficher(self):
        print("Grille\n")
        for i in range(self.size):
            print(self.matrix[i])

    def testGrille(self, row=0, column=0, value=0):
        completed = True;
        verified = self.ValueInBlock(row, column, value)
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] <= 0:
                    completed = False;
                if self.matrix[i][j] == value:
                    if i == row or j == column:
                        verified = False
                        print("Le nombre", value, "existe deja dans en", i, j, )
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
        return unique;

    def estRemplie(self):
        completed = True;
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] <= 0:
                    completed = False;

        return completed