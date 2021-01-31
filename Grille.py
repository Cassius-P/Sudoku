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

        # Création du sudoku complet (avec toutes les valeurs) via pattern
        self.boardComplete = [[nums[self.pattern(r, c)] for c in cols] for r in rows]
        for i in range(self.size):
            print(self.boardComplete[i])

    #Création et retour de la grille vidée de certaines valeurs
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
    #Retourne grille complète
    def getCompleteGrille(self):
        return self.boardComplete

    def pattern(self, row, col):
        return (self.base*(row%self.base)+row//self.base+col)%(self.side)

    # Randomizer pour création aléatoire de Sudoku
    def shuffle(self, s):
        return sample(s, len(s))

    #Retourne valeur via coordonnées ( ligne, colonne) dans la matrice
    def getValeur(self, row, column):
        print(self.matrix[row][column])

    #Définition d'un valeur via (ligne, colonne) dans la matrice
    def setValeur(self, value, shown, row, column):
        if shown == False:
            value = -value
        self.matrix[row][column] = value

    #Affichage grilles dans la console
    def afficher(self):
        print("Grille imcomplete\n")
        for i in range(self.size):
            print(self.boardIncomplete[i])

        print("\n Complete")
        for i in range(self.size):
            print(self.boardComplete[i])
    #Définition de la grille lors de chargement d'une partie par l'utilisateur
    def setGrid(self, grid):
        self.boardComplete = grid[0]
        self.board = grid
