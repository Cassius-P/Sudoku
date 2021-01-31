from Game import *
from PyQt5.QtWidgets import *
from Game import *
import sys

app = QApplication(sys.argv)
class Sudoku():
    def __init__(self, size = 9):

        self.window = Game(size=size)
        self.window.setWindowTitle("Sudoku")
        self.window.show()
        sys.exit(app.exec_())

class HomeScreen():
    def __init__(self):
        self.window = HomeScreen()
        self.window("sudoku")
        self.window.show()
        sys.exit(app.exec_())

class Handler():
    def __init__(self):
        return self


    def caseBorder(self,painter, option, ligne):
        self.window.caseBorder(painter, option, ligne)
