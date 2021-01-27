from Window import *
from PyQt5.QtWidgets import *
from Window import *
import sys


class Sudoku():
    def __init__(self, size = 9):
        app = QApplication(sys.argv)
        self.window = Window(size=size)
        self.window.setWindowTitle("Sudoku")
        self.window.show()
        sys.exit(app.exec_())


class Handler():
    def __init__(self):
        return self


    def caseBorder(self,painter, option, ligne):
        self.window.caseBorder(painter, option, ligne)
