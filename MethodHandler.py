from Window import *
from ItemDelegate import *
from PyQt5.QtWidgets import *
import sys


class Sudoku():

    def __init__(self, size = 9):
        app = QApplication(sys.argv)
        self.window = Window()
        self.window.setWindowTitle("Sudoku")
        self.window.show()
        sys.exit(app.exec_())


class Handler():
    def caseBorder(self,painter, option, ligne):
        self.window.caseBorder(painter, option, ligne)
