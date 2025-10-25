# 🧩 Sudoku Solver
A minimalistic Sudoku solver that fills in empty cells using logical deduction and backtracking.

**Input Format**  
Use `0` to represent empty cells.

**Test Case – Input Grid:**
```
0 0 0 0 0 0 5 9 0  
0 4 0 0 0 0 8 1 3  
5 0 1 0 0 0 0 2 0  
7 0 3 0 1 0 0 4 0  
0 0 0 0 0 3 0 0 5  
0 0 8 5 0 0 3 6 9  
9 0 0 8 0 0 0 0 0  
1 8 5 9 0 2 7 0 0  
0 0 0 0 0 6 0 0 2
```

**Expected Output:**
```
8 2 7 3 6 1 5 9 4  
6 4 9 7 2 5 8 1 3  
5 3 1 4 9 8 6 2 7  
7 5 3 6 1 9 2 4 8  
4 9 6 2 8 3 1 7 5  
2 1 8 5 7 4 3 6 9  
9 6 2 8 3 7 4 5 1  
1 8 5 9 4 2 7 3 6  
3 7 4 1 5 6 9 8 2
```

---

### 🖼️ Sudoku Solver GUI
A second version of the program includes a **Tkinter-based graphical interface**, allowing users to:

- Input Sudoku puzzles manually
- Visualize the solving process
- Reset or load new puzzles
- View the solution in real time

