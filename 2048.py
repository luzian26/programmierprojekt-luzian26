# Imports
import tkinter as tk
import colors as c
import random

# Klassen definieren
class Game2048:
    pass



class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title('2048')
        self.main_grid = Board(self)
        self.score_board = ScoreBoard(self)
        self.matrix = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
        
        #self.mainloop()
        #self.start_game()

    def start_game(self):
        self.add_new_cell()

    def add_new_cell(self):
        freie_Felder = []
        for row in range(0, 4):
            for col in range(0, 4):
                if self.matrix[row][col] == 0:
                    freie_Felder.append((row, col))

        print(freie_Felder)

    def start_game(self):
        pass
       

class Board(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.config(bg=c.GRID_COLOR, bd=3, width=400, height=400)
        self.grid(row=1, column=0)
        self.cells = []
        for row in range(0, 4):
            self.cells.append([])
            for col in range(0, 4):
                self.cells[row].append(Cell(self, row, col))
        
    def configure_cell(row:int, col:int, value:int):
        pass

class Cell(tk.Frame):
    def __init__(self, parent, row, col):
        self.frame = tk.Frame(parent, bg=c.EMPTY_CELL_COLOR, width=100, height=100)
        self.number = tk.Label(parent, bg=c.EMPTY_CELL_COLOR)
        self.frame.grid(row=row, column=col, padx=5, pady=5)
        self.number.grid(row=row, column=col)
        tk.Frame.__init__(self, parent)
        self.config(bg=c.EMPTY_CELL_COLOR,
            width=100,
            height=100)
        self.grid(row=row, column=col, padx=5, pady=5)

        self.number = tk.Label(
            self,
            bg=c.EMPTY_CELL_COLOR)
        self.number.place(relx=0.5, rely=0.5, anchor="center")

        
    def configure(self, value):
        if value == 0:
            self.config(bg=c.EMPTY_CELL_COLOR)
            self.number.config(
                bg=c.EMPTY_CELL_COLOR, text="")
        else:
            self.config(
                bg=c.CELL_COLORS[value])
            self.number.config(
                bg=c.CELL_COLORS[value],
                fg=c.CELL_NUMBER_COLORS[value],
                font=c.CELL_NUMBER_FONTS[value],
                text=str(value))

  

class ScoreBoard(tk.Frame):
    def __init__(self, parent):
        self.score = 0
        self.frame = tk.Frame
        self.label = tk.Label 
        tk.Frame.__init__(self, parent)
        self.grid(row=0, column=0, pady=10)

        tk.Label(self, text="Score", font=c.SCORE_LABEL_FONT).grid(row=0)
        tk.Label(self, text=self.score, font=c.SCORE_FONT).grid(row=1)

    def add_to_score(plus:int):
        pass 
    def configure():
        pass 




# Spiel spielen
if __name__ == "__main__":
    root = tk.Tk()
    myGame = Game()
    myGame.start_game()
    root.mainloop()
 