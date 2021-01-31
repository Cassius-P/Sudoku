from math import *


class VerifGrid:
    def __init__(self, grid, size: int):
        self.gridToVerify = grid;
        self.gridSize = size;

        self.statut = self.valid_board()

    def getStatut(self):
        return self.statut

    def factVerif(self, numberArray):
        temp = 1
        for i in numberArray:
            temp = temp * i

        #print(temp, factorial(self.gridSize))
        return temp != factorial(self.gridSize)

    def valid_row(self, row: int, grid):

        temp = grid[row]
        # Removing 0's.
        temp = list(filter(lambda a: a != 0, temp))
        # Checking for invalid values.
        if any(i < 0 and i > self.size for i in temp):
            print("Invalid value")
            return -1
        # Checking for repeated values.
        elif len(temp) != len(set(temp)):
            return 0
        else:
            return 1

    def valid_col(self, col, grid):

        # Extracting the column.
        temp = [row[col] for row in grid]
        # Removing 0's.
        temp = list(filter(lambda a: a != 0, temp))
        # Checking for invalid values.
        if any(i < 0 and i > self.size for i in temp):
            print("Invalid value")
            return -1
        # Checking for repeated values.
        elif len(temp) != len(set(temp)):
            return 0
        else:
            return 1

    def valid_subsquares(self, grid):
        sqr = int(sqrt(self.gridSize))
        for row in range(0, self.gridSize, sqr):
            for col in range(0, self.gridSize, sqr):
                #print("Row - col", row, "-", col)
                temp = []
                for r in range(row, row + sqr):
                    for c in range(col, col + sqr):
                        if grid[r][c] != 0:
                            temp.append(grid[r][c])
                # Checking for invalid values.
                if any(i < 0 and i > self.size for i in temp):
                    print("Invalid value")
                    return -1
                # Checking for repeated values.
                elif self.factVerif(temp):
                    return 0
        return 1

    # Function to check if the board invalid.
    def valid_board(self):
        for i in range(self.gridSize):
            # print(i)
            res1 = self.valid_row(i, self.gridToVerify)
            res2 = self.valid_col(i, self.gridToVerify)

            if (res1 < 1 or res2 < 1):
                print("The board is invalid")
                return "Grille invalide"

        res3 = self.valid_subsquares(self.gridToVerify)
        if (res3 < 1):
            return "Grille invalide"
        else:
            return "Grille valide, Bravo !"

