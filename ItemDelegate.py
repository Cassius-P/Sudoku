from __future__ import division
from math import *
from PyQt5.QtWidgets import *
from MethodHandler import *

from Window import *


class ItemDelegate(QItemDelegate):

    def __init__(self, parent=None):
        super(ItemDelegate, self).__init__(parent)
        self.handler = Handler()

    def grilleinit(self, grille, size):
        self.grille = grille
        self.size = size

    def paint(self, painter, option, index):

        row, col = index.row(), index.column()
        if row == 0:
            self.handler.caseBorder(painter, option, 'h')
        elif (row + 1) % sqrt(self.size) == 0:
            self.handler.caseBorder(painter, option, 'b')

        if col == 0:
            self.handler.caseBorder(painter, option, 'g')
        elif (col + 1) % sqrt(self.size) == 0:
            self.handler.caseBorder(painter, option, 'd')

        QItemDelegate.paint(self, painter, option, index)
