# Imports
import tkinter as tk
import colors as c


# Klassen definieren
class Game2048:
    pass



class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title('2048')
        self.main_grid = Board(self)
        self.mainloop()

class Board(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self)
        tk.Frame(self, bg=c.GRID_COLOR, bd=3, width=400, height=400)
        self.grid(pady=(80, 0))

    def configure_cell(row:int, col:int, value:int):
        pass

class Cell():
    def __init__(self, parent, row, col):
        self.frame = tk.Frame(parent, bg=c.EMPTY_CELL_COLOR, width=100, height=100)
        self.number = tk.Label(parent, bg=c.EMPTY_CELL_COLOR)
        self.frame.grid(row=row, column=col, padx=5, pady=5)
        self.number.grid(row=row, column=col)

    def configure(value:int):
        pass

  

class ScoreBoard():
    def __init__(self):
        self.score = 0
        frame = tk.Frame
        label = tk.Label

    def add_to_score(plus:int):
        pass 
    def configure():
        pass 




# Spiel spielen
if __name__ == "__main__":
    # myGame = Game2048()
    # myGame.start_game()
    pass