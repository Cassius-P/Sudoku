from __future__ import division

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtCore, QtGui

class Window(QWidget):

    def __init__(self, parent=None, size = 9):
        super(Window, self).__init__(parent)

        # crée la grille 9x9
        self.table = QTableWidget(self)
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
                tableItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.table.setItem(row, col, tableItem)

        # définit la police de caractère par défaut de la table
        font = QFont()
        font.setFamily(u"DejaVu Sans")
        font.setPointSize(16)
        self.table.setFont(font)

        # taille de la fenêtre
        self.resize(53 * 9, 53 * 9)

        # positionne la table dans la fenêtre
        posit = QGridLayout()
        posit.addWidget(self.table, 0, 0)
        self.setLayout(posit)

        # Grille test
        self.grilleTest = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        # intégre le delegate pour lignes en gras et les cases en couleur
        self.delegate = MonDelegate(self.table)
        self.table.setItemDelegate(self.delegate)

        # redessine les lignes en gras et les cases de couleur
        self.delegate.grilleinit(self.grilleTest)

        # affiche la grille courante
        self.showGrille(self.grilleTest)

        # place le focus
        self.table.setFocus()
        self.table.setCurrentCell(0, 0)

    def showGrille(self, grille):

        for row in range(len(grille[0])):
            for col in range(len(grille)):
                if grille[row][col] == 0:
                    self.table.item(row, col).setText(u"")
                    self.table.item(row, col).setFlags(
                        QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable)
                else:
                    self.table.item(row, col).setText(str(grille[row][col]))
                    self.table.item(row, col).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)


    def setCouleur(self, coordinates):
        #couleur = QColor(160, 255, 160, 255)  # vert clair
        #self.table.item(2, 4).setBackground(couleur)

        #couleur = QColor(255, 160, 160, 255)  # rouge clair
        #self.table.item(6, 3).setBackground(couleur)
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


#############################################################################
class MonDelegate(QItemDelegate):

    # ========================================================================
    def __init__(self, parent=None):
        super(MonDelegate, self).__init__(parent)

    # ========================================================================
    def grilleinit(self, g):
        self.g0 = g

    # ========================================================================
    def paint(self, painter, option, index):
        """appelé case par case pour en dessiner le contenu"""

        row, col = index.row(), index.column()
        if row == 0 or row == 3 or row == 6:
            if col in [0, 3, 6]:
                Window.caseBorder(painter, option, 'g')
                Window.caseBorder(painter, option, 'h')
            elif col == 8:
                Window.caseBorder(painter, option, 'd')
                Window.caseBorder(painter, option, 'h')
            else:
                Window.caseBorder(painter, option, 'h')
        elif row in [1, 2, 4, 5, 7]:
            if col in [0, 3, 6]:
                Window.caseBorder(painter, option, 'g')
            elif col == 8:
                Window.caseBorder(painter, option, 'd')
        elif row == 8:
            if col in [0, 3, 6]:
                Window.caseBorder(painter, option, 'g')
                Window.caseBorder(painter, option, 'b')
            elif col == 8:
                Window.caseBorder(painter, option, 'd')
                Window.caseBorder(painter, option, 'b')
            else:
                Window.caseBorder(painter, option, 'b')

                # mettre la couleur souhaitée dans les cases de départ ayant un numéro


        QItemDelegate.paint(self, painter, option, index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fen = Window()
    fen.setWindowTitle("Sudoku")
    fen.show()
    sys.exit(app.exec_())


