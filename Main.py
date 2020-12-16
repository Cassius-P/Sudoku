from tkinter import *
from math import *

def clicked(event):
    print("pressed")

def main():
    value = 9

    fenetre = Tk(className="Sudoku", screenName="Sudoku", baseName="Sudoku")
    fenetre.geometry("1000x700")

    canvas = Canvas(fenetre, relief=FLAT, background="black", width=value*100+sqrt(value), height=value*100+sqrt(value))
    canvas.pack()
    label = Label(fenetre, text="Hello world")
    label.pack()

    for i in range(value):
        for j in range(value):
            blockI = 99
            blockJ = 99
            if (j % sqrt(value) == 0):
                blockJ = 95

            if (i % sqrt(value) == 0):
                blockI = 95

            coordinatesX = 100 * (j + 1)
            coordinatesY = 100 * (i + 1)
            canvas.create_rectangle(coordinatesX - blockJ, coordinatesY - blockI, coordinatesX, coordinatesY,
                                    fill="white", outline="black")
            

    fenetre.mainloop()

main()



