import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.



for i in range(9):
    Sudoku.append(n)

Answer_Row = True
Answer_Col = True
Answer_Sub = True


for i in range(9):
    for x in Sudoku_numbers:
        if x not in Sudoku[i]:
Counter_True = 0
Counter_False = 0
for i in range(9):
    for x in Sudoku_numbers:
        for j in range(9):
            if x not in Sudoku[j][i]:



for i in range(3):
        Sudoku_Subhelp = Sudoku_Subhelp + Sudoku[j][(i*3):((i*3)+3)]
    Sudoku_Subgrid.append(Sudoku_Subhelp)
for i in range(3):
    for j in range(3, 6):
        Sudoku_Subhelp = Sudoku_Subhelp + Sudoku[j][(i*3):((i*3)+3)]
    Sudoku_Subgrid.append(Sudoku_Subhelp)
for i in range(3):
    for j in range(6, 9):
        Sudoku_Subhelp = Sudoku_Subhelp + Sudoku[j][(i*3):((i*3)+3)]
    Sudoku_Subgrid.append(Sudoku_Subhelp)
for i in range(9):
    for x in Sudoku_numbers:
        if x not in Sudoku_Subgrid[i]:

    print("true")
else:
    print("false")
