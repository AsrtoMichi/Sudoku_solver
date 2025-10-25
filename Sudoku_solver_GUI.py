"""
A GUI that allow to solve easely sudoku
"""
from typing import List
from tkinter import Tk, Entry, IntVar
from tkinter.messagebox import showerror
from tkinter.ttk import Frame, Button

__autor__ = "Michele Gallo"
__date__ = "03/08/2024"


class App(Tk):
    def __init__(self):

        super().__init__()
        self.title('Sudoku solver')
        self.resizable(False, False)

        frame = Frame(self)
        frame.pack()

        self.intvar_list = [[IntVar() for _ in range(9)]
                            for _ in range(9)]

        for y in range(9):
            for x in range(9):
                Entry(frame, width=6, textvariable=self.intvar_list[x][y]).grid(
                    column=x, row=y)

        Button(self, text="Solve", command=self.solve_GUI).pack()
        # self.bind("<Enter>", lambda key: self.solve_GUI())

        Button(self, text="Clear", command=self.clear).pack()

    def solve_GUI(self):

        grid = [[intvar.get()for intvar in column]
                for column in self.intvar_list]

        if self.ceck_correctes(grid) and Suduko(grid):

            for i in range(9):
                for j in range(9):
                    self.intvar_list[i][j].set(grid[i][j])

        else:
            showerror("Error", "Solution does not exist :(")
            #self.clear()

    def clear(self):
        for column in self.intvar_list:
            for intvar in column:
                intvar.set(0)

    def ceck_correctes(self, grid: List[List[int]]) -> bool:

        def find_duplicate(grid: List[List[int]], row: int, col: int, num: int) -> bool:
            for x in set(range(9)).difference({row}):
                if grid[row][x] == num:
                    return True

            for x in set(range(9)).difference({col}):
                if grid[x][col] == num:
                    return True

            startRow = row - row % 3
            startCol = col - col % 3
            for i in range(startRow, startRow + 3):
                for j in range(startCol, startCol + 3):
                    if grid[i][j] == num and (i != row or j != col):
                        return True
            return False

        for y in range(9):
            for x in range(9):
                if grid[y][x] != 0 and find_duplicate(grid, y, x, grid[y][x]):
                    return False

        return True


def Suduko(grid: List[List[int]], row: int = 0, col: int = 0) -> bool:

    def _solve(grid: List[List[int]], row: int, col: int, num: int) -> bool:
        for x in range(9):
            if grid[row][x] == num:
                return False

        for x in range(9):
            if grid[x][col] == num:
                return False

        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                if grid[i][j] == num:
                    return False
        return True

    if row == 8 and col == 9:
        return True
    if col == 9:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, 10):

        if _solve(grid, row, col, num):

            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True

        grid[row][col] = 0
    return False


if __name__ == "__main__":
    App().mainloop()
