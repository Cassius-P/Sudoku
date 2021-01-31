from __future__ import division
from math import *
from PyQt5.QtGui import QFont, QResizeEvent, QColor
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from VerifGrid import *
from Grille import Grille
import keyboard
import time
import sys


class Game(QWidget):

    def __init__(self, parent=None, size=int, load=[]):
        super().__init__(parent)
        # crée la grille et le bouton de verif

        self.table = QTableWidget(self)
        self.table.itemChanged.connect(self.changeValue)


        #Verification button
        verif = QPushButton("Verifier grille")
        verif.clicked.connect(self.verifButton)
        self.verif = verif

        #Save Game button
        save = QPushButton("Sauvegarder")
        save.clicked.connect(self.saveGame)
        self.save = save


        self.size = size
        self.table.setRowCount(self.size)
        self.table.setColumnCount(self.size)

        # Cache les entêtes horizontale et verticale
        self.table.horizontalHeader().hide()
        self.table.verticalHeader().hide()

        # Définit les cases carrées 50 pixels x 50 pixels
        for row in range(self.size):
            self.table.setRowHeight(row, 50)
            for col in range(self.size):
                self.table.setColumnWidth(col, 50)

        # remplit la grille avec des QTableWidgetItem
        for row in range(self.size):
            for col in range(self.size):
                tableItem = QTableWidgetItem()
                # val= self.testGrid[row][col]
                tableItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                # tableItem.setText(str(val))
                self.table.setItem(row, col, tableItem)

        # définit la police de caractère par défaut de la table
        font = QFont()
        font.setFamily(u"DejaVu Sans")
        font.setPointSize(16)
        self.table.setFont(font)

        # taille de la fenêtre
        self.setFixedSize(52 * self.size +6, 53 * self.size + 55)

        # positionne la table dans la fenêtre
        posit = QGridLayout()
        posit.addWidget(self.table, 0, 0)
        #posit.addWidget(self.timer, 88 * self.size, 0)
        posit.addWidget(self.verif, 52 * self.size,0)
        posit.addWidget(self.save, 75 * self.size, 0)

        self.setLayout(posit)

        # Grille test
        self.grilleTest = Grille(self.size)
        print("Load : ", load)

        #Chargement de la grille pour chargée et nouvelle partie
        if len(load) == 0:
            print("New game detected")
            self.full = self.grilleTest.getCompleteGrille()

            self.startMatrix = self.grilleTest.getGrille()
            self.matrix = self.startMatrix
        else:
            print("Loaded game detectd")
            self.full = load[1]
            self.grilleTest.setGrid(load)
            self.startMatrix = load[0]
            self.matrix = load[2]
            print("loaded")

        # intégre le delegate pour lignes en gras et les cases en couleur
        self.delegate = ItemDelegate(self.table)
        self.table.setItemDelegate(self.delegate)

        # redessine les lignes en gras et les cases de couleur
        self.delegate.grilleinit(self.matrix, self.size)

        # affiche la grille courante
        self.showGrille(self.matrix)

        # place le focus
        self.table.setFocus()
        self.table.setCurrentCell(0, 0)


    #Verification d'une grille
    def verifButton(self):
        for i in range(self.size):
            print(self.matrix[i])
        verif = VerifGrid(self.matrix, self.size)
        self.verif.setText(verif.getStatut())
        self.verif.setDisabled(True)

    #Enregistrement d'une partie
    def saveGame(self):
        infos = [self.startMatrix, self.full, self.matrix]
        print('\n' + self.formatNumbers(infos[0]))
        with open(str(time.time())+".sudoku", 'w')as file:
            print(file)
            file.write(self.formatNumbers(infos[0]) + "\n")
            file.write(self.formatNumbers(infos[1]) + "\n")
            file.write(self.formatNumbers(infos[2]) + "\n")
            file.close()

        self.save.setText("Sauvegardé !")
        self.save.setDisabled(True)
    #Formatage de la date pour l'enregistrement du fichier de sauvegarde
    def formatNumbers(self, array):
        sep = ''
        stringList = []
        for n1 in array:
            for n2 in n1:
                stringList.append(str(n2))
        return sep.join(stringList)


    #event quand une case de la grille change de valeur
    def changeValue(self):
        ac = self.table.currentItem()
        if (isinstance(ac, QTableWidgetItem)):
            row = ac.row()
            col = ac.column()
            try:
                indice = False
                if (keyboard.is_pressed('ctrl')):
                    indice = True
                if (self.size == 9):
                    val = int(ac.text())
                    if(val < self.size):
                        self.matrix[row][col] = val if indice != True else 0
                        self.setCouleur((row, col), QColor(255, 255, 255) if indice != True else QColor(51, 153, 255));
                        self.save.setText("Sauvegarder")
                        self.save.setDisabled(False)
                        self.verif.setText("Vérifier grille")
                        self.verif.setDisabled(False)
                    else:
                        self.table.item(row, col).setText('')
                else:
                    print("Grid of 16")

            except ValueError:
                print("pas un nombre")
                self.table.item(row, col).setText('');
                # self.setCouleur((row, col), QColor(240,0,0))


    #Affichage de la grille de départ avec remplssage des valeurs
    def showGrille(self, grille):
        for row in range(self.size):
            for col in range(self.size):
                #Si la valeur vaut 0, affichage casse vide
                if grille[row][col] == 0:
                    self.table.item(row, col).setText(u"")
                    self.table.item(row, col).setFlags(
                        QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable)
                #Si valeur différente de 0 affichage valeur non modifiable par utilisateur
                else:
                    self.table.item(row, col).setText(str(grille[row][col]))
                    self.table.item(row, col).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)

                    #Mise en évidence des valeurs non modifiables
                    font = QFont()
                    font.setWeight(70)
                    self.table.item(row, col).setFont(font)

                    # Détruit le design (grille) donc commenté
                    # self.table.item(row, col).setBackground(QColor(228, 228, 228))

    #Changement de la couleur d'une case
    def setCouleur(self, coordinates, color):
        x, y = coordinates
        self.table.item(x, y).setBackground(color)
        return True

    #Bordure des cases avec 'bold' pour sépration des blocs
    def caseBorder(painter, option, ligne):
        r = option.rect
        x, y, w, h = r.x(), r.y(), r.width(), r.height()
        if ligne == 'h':
            x1, y1, x2, y2 = x, y, x + w, y
        elif ligne == 'd':
            x1, y1, x2, y2 = x + w, y, x + w, y + h
        elif ligne == 'b':
            x1, y1, x2, y2 = x + w, y + h, x, y + h
        elif ligne == 'g':
            x1, y1, x2, y2 = x, y + h, x, y
        else:
            return
        pen = QtGui.QPen()
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawLine(x1, y1, x2, y2)

#ItemDelagate pour les items de la table, class QTableWidgetItem
class ItemDelegate(QItemDelegate):

    def __init__(self, parent=None):
        super(ItemDelegate, self).__init__(parent)

    def grilleinit(self, grille, size):
        self.grille = grille
        self.size = size


    #Definition des bordures cf ligne 195
    def paint(self, painter, option, index):

        row, col = index.row(), index.column()
        if row == 0:
            Game.caseBorder(painter, option, 'h')
        elif (row + 1) % sqrt(self.size) == 0:
            Game.caseBorder(painter, option, 'b')
        if col == 0:
            Game.caseBorder(painter, option, 'g')
        elif (col + 1) % sqrt(self.size) == 0:
            Game.caseBorder(painter, option, 'd')

        QItemDelegate.paint(self, painter, option, index)
