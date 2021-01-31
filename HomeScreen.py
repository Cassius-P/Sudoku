from PyQt5.QtGui import QFont, QResizeEvent, QColor, QIcon
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from Game import *


class HomeScreenC(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None  # No external window yet.
        self.setWindowTitle("Sudoku Launcher")
        self.setWindowIcon(QIcon('icon.png'))

        #Bouton pour charger une partie
        self.load = QPushButton("Charger une partie")
        self.load.clicked.connect(self.chargerPartie)

        #Bouton pour créér une nouvelle partie
        self.newGame = QPushButton("Nouvelle partie")
        self.newGame.clicked.connect(self.startGame)

        posit = QVBoxLayout()
        posit.addWidget(self.load)
        posit.addWidget(self.newGame)

        #Widget pour affichage des boutons
        view = QWidget()
        view.setLayout(posit)

        self.setCentralWidget(view)

    #Création d'une nouvelle fenetre/partie avec grille vide
    def startGame(self):
        self.w = Game(size=9)
        self.w.setWindowTitle("Sudoku")

        self.w.setWindowIcon(QIcon('icon.png'))
        self.w.show()
        self.close()

    #Création d'une nouvelle fenêtre/partie avec grille chargée par une sauvegarde
    def chargerPartie(self):
        fileName, _ = QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.rootPath(), '*.sudoku')
        if fileName != "":
            with open(fileName) as f:
                contenu = f.readlines()

            gridSize = int(sqrt(len(contenu[0].replace('\n', ''))))

            save = []

            for line in contenu:
                line = line.replace('\n', '')
                line = [line[i:i + gridSize] for i in range(0, len(line), gridSize)]

                row = []
                for number in line:
                    row.append([int(number[i:i+1]) for i in range(0, len(number), 1)])
                line = row
                print(line)
                save.append(line)
            print(save)

            self.w = Game(size=gridSize, load=save)
            self.w.setWindowTitle("Sudoku")

            self.w.setWindowIcon(QIcon('icon.png'))
            self.w.show()
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = HomeScreenC()
    w.show()
    app.exec_()
