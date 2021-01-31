from __future__ import division
from math import *
from PyQt5.QtGui import QFont, QResizeEvent, QColor
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from VerifGrid import *
from Grille import Grille
import keyboard
import sys

class Game(QWidget):

    def __init__(self, parent=None, size=int):
        super(Game, self).__init__(parent)

        # crée la grille et le boutonde verif
        self.table = QTableWidget(self)
        self.table.itemChanged.connect(self.changeValue)

        button = QPushButton("Verifier grille")
        button.clicked.connect(self.verifButton)
        self.verif = button

        self.size = size
        self.table.setRowCount(self.size)
        self.table.setColumnCount(self.size)

        # cache les entêtes horizontale et verticale
        self.table.horizontalHeader().hide()
        self.table.verticalHeader().hide()

        # définit les cases carrées 50 pixels x 50 pixels
        for row in range(self.size):
            self.table.setRowHeight(row, 50)
            for col in range(self.size):
                self.table.setColumnWidth(col, 50)


        # remplit la grille avec des QTableWidgetItem
        for row in range(self.size):
            for col in range(self.size):

                tableItem = QTableWidgetItem()
                #val= self.testGrid[row][col]
                tableItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                #tableItem.setText(str(val))
                self.table.setItem(row, col, tableItem)

        # définit la police de caractère par défaut de la table
        font = QFont()
        font.setFamily(u"DejaVu Sans")
        font.setPointSize(16)
        self.table.setFont(font)

        # taille de la fenêtre
        self.setFixedSize(52 * self.size+88, 53 * self.size + 26)

        # positionne la table dans la fenêtre
        posit = QGridLayout()
        posit.addWidget(self.table, 0, 0)
        posit.addWidget(self.verif, 52 * self.size, 52 * self.size)
        self.setLayout(posit)

        # Grille test
        self.grilleTest = Grille(self.size)
        self.full = self.grilleTest.getCompleteGrille()

        self.startMatrix = self.grilleTest.getGrille()
        self.matrix = self.startMatrix

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


    def verifButton(self):
        for i in range(self.size):
            print(self.matrix[i])
        VerifGrid(self.matrix, self.size)

    def changeValue(self):
        ac = self.table.currentItem()
        if(isinstance(ac, QTableWidgetItem)):
            row = ac.row()
            col = ac.column()
            try:
                indice = False
                if(keyboard.is_pressed('ctrl')):
                    indice= True
                if(self.size == 9):
                    val = int(ac.text())

                    self.matrix[row][col] = val if indice != True else 0
                    self.setCouleur((row,col), QColor(255,255,255) if indice != True else QColor(51, 153, 255));
                else:
                    print("Grid of 16")

                #self.grilleTest.afficher()
                # print("un nombre", val, "row", row, "col", col, "\n")
            except ValueError:
                print("pas un nombre")
                self.table.item(row, col).setText('');
                #self.setCouleur((row, col), QColor(240,0,0))




    def showGrille(self, grille):
        for row in range(self.size):
            for col in range(self.size):
                if grille[row][col] == 0:
                    self.table.item(row, col).setText(u"")
                    self.table.item(row, col).setFlags(
                        QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable )
                else:
                    self.table.item(row, col).setText(str(grille[row][col]))
                    self.table.item(row, col).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)

                    font = QFont()
                    font.setWeight(70)
                    self.table.item(row, col).setFont(font)

                    #Détruit le design (grille)
                    #self.table.item(row, col).setBackground(QColor(228, 228, 228))

    def setCouleur(self, coordinates, color):
        x,y = coordinates
        self.table.item(x, y).setBackground(color)
        return True

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

class ItemDelegate(QItemDelegate):

    def __init__(self, parent=None):
        super(ItemDelegate, self).__init__(parent)


    def grilleinit(self, grille, size):
        self.grille = grille
        self.size = size

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


