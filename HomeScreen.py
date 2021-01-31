from PyQt5.QtGui import QFont, QResizeEvent, QColor
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from MethodHandler import *

class HomeScreenC(QWidget):
    def __init__(self,parent=None):
        super(HomeScreenC, self).__init__(parent)
        print("boooooo")
        button = QPushButton("Charger la partie")
        button.clicked.connect(self.chargerPartie)

        posit = QGridLayout()
        posit.addWidget(button, 0, 0)

        self.setLayout(posit)



    def jsp(self):
        print("jsp")

    def chargerPartie(self):
        fileName, _ = QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.rootPath(), '*.xlsm')
        with open(fileName) as f:
            contenu = f.readlines()
        contenu = [x.strip() for x in contenu]

        self.grille = []
        for ligne in contenu:
            self.grille.append([int(x) for x in ligne.split()])
        Sudoku(9,self.grille)
