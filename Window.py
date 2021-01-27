from __future__ import division
from math import *
from PyQt5.QtGui import QFont, QResizeEvent
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui

from Grille import Grille
import sys

class Window(QWidget):

    def __init__(self, parent=None, size=int):
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
        self.setFixedSize(52 * self.size +250, 53 * self.size)

        # positionne la table dans la fenêtre
        posit = QGridLayout()
        posit.addWidget(self.table, 0, 0)
        self.setLayout(posit)

        # Grille test
        self.grilleTest = Grille(self.size).getGrille()

        # intégre le delegate pour lignes en gras et les cases en couleur
        self.delegate = ItemDelegate(self.table)
        self.table.setItemDelegate(self.delegate)

        # redessine les lignes en gras et les cases de couleur
        self.delegate.grilleinit(self.grilleTest, self.size)

        # affiche la grille courante
        self.showGrille(self.grilleTest)

        # place le focus
        self.table.setFocus()
        self.table.setCurrentCell(0, 0)

    def showGrille(self, grille):
        for row in range(self.size):
            for col in range(self.size):
                if grille[row][col] == 0:
                    self.table.item(row, col).setText(u"")
                    self.table.item(row, col).setFlags(
                        QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable)
                else:
                    self.table.item(row, col).setText(str(grille[row][col]))
                    self.table.item(row, col).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)

    def setCouleur(self, coordinates):
        # couleur = QColor(160, 255, 160, 255)  # vert clair
        # self.table.item(2, 4).setBackground(couleur)

        # couleur = QColor(255, 160, 160, 255)  # rouge clair
        # self.table.item(6, 3).setBackground(couleur)
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
            Window.caseBorder(painter, option, 'h')
        elif (row + 1) % sqrt(self.size) == 0:
            Window.caseBorder(painter, option, 'b')

        if col == 0:
            Window.caseBorder(painter, option, 'g')
        elif (col + 1) % sqrt(self.size) == 0:
            Window.caseBorder(painter, option, 'd')

        QItemDelegate.paint(self, painter, option, index)




class QCustomTableWidget (QTableWidget):
    def __init__ (self, parent = None):
        super(QCustomTableWidget, self).__init__(parent)
        # Setup row & column data
        listsVerticalHeaderItem = ['Device 1', 'Device 2', 'Device 3', 'Device 4', 'Device 5']
        self.setRowCount(len(listsVerticalHeaderItem))
        for index in range(self.rowCount()):
            self.setVerticalHeaderItem(index, QTableWidgetItem(listsVerticalHeaderItem[index]))
        listsVerticalHeaderItem = ['Device 1', 'Device 2', 'Device 3', 'Device 4']
        self.setColumnCount(5)
        listsHorizontalHeaderItem = ['Option 1', 'Option 2']
        self.setColumnCount(len(listsHorizontalHeaderItem))
        for index in range(self.columnCount()):
            self.setHorizontalHeaderItem(index, QTableWidgetItem(listsHorizontalHeaderItem[index]))

    def dataChanged (self, topLeftQModelIndex, bottomRightQModelIndex):
        row,column = topLeftQModelIndex
        dataQTableWidgetItem = self.item(row, column)
        print('###### Data Changed  ######')
        print ('row    :', row + 1)
        print ('column :', column + 1)
        #self.connectNotify(QtCore.SIGNAL('dataChanged'), row, column, dataQTableWidgetItem)
        QTableWidget.dataChanged(self, topLeftQModelIndex, bottomRightQModelIndex)

class QCustomWidget (QWidget):
    def __init__(self, parent = None):
        super(QCustomWidget, self).__init__(parent)
        self.myQCustomTableWidget = QCustomTableWidget(self)
        self.myQLabel = QLabel('Track edited data', self)
        myQVBoxLayout = QVBoxLayout()
        myQVBoxLayout.addWidget(self.myQLabel)
        myQVBoxLayout.addWidget(self.myQCustomTableWidget)
        self.setLayout(myQVBoxLayout)
        self.myQCustomTableWidget.dataChanged((0,0),(15,15))

    def setTrackData (self, row, column, dataQTableWidgetItem):
        self.myQLabel.setText('Last updated\nRow : %d, Column : %d, Data : %s' % (row + 1, column + 1, str(dataQTableWidgetItem.text())))

if __name__ == '__main__':
    myQApplication = QApplication(sys.argv)
    myQCustomWidget = QCustomWidget()
    myQCustomWidget.show()
    sys.exit(myQApplication.exec_())