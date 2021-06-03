import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

Sudoku=[]
Sudoku_numbers = ["1","2","3","4","5","6","7","8","9"]


for i in range(9):
    n= input().split()
    Sudoku.append(n)

Answer_Row = True
Answer_Col = True
Answer_Sub = True


for i in range(9):
    for x in Sudoku_numbers:
        if x not in Sudoku[i]:
            Answer_Row=False
        
Counter_True = 0
Counter_False = 0
       
for i in range(9):
    for x in Sudoku_numbers:
        Counter_False=0
        for j in range(9):
            
            if x not in Sudoku[j][i]:
                Counter_False+=1
        if Counter_False!=8 and j==8:
            Answer_Col=False


Sudoku_Subgrid=[]

for i in range(3):
    Sudoku_Subhelp=[]
    for j in range(3):  
        Sudoku_Subhelp = Sudoku_Subhelp + Sudoku[j][(i*3):((i*3)+3)]
    Sudoku_Subgrid.append(Sudoku_Subhelp)
for i in range(3):
    Sudoku_Subhelp=[]
    for j in range(3, 6):
        Sudoku_Subhelp = Sudoku_Subhelp + Sudoku[j][(i*3):((i*3)+3)]
    Sudoku_Subgrid.append(Sudoku_Subhelp)
for i in range(3):
    Sudoku_Subhelp=[]
    for j in range(6, 9):
        Sudoku_Subhelp = Sudoku_Subhelp + Sudoku[j][(i*3):((i*3)+3)]
    Sudoku_Subgrid.append(Sudoku_Subhelp)
    
for i in range(9):
    for x in Sudoku_numbers:
        if x not in Sudoku_Subgrid[i]:
                Answer_Sub=False

if Answer_Row == Answer_Col == Answer_Sub == True:
    print("true")
else:
    print("false")

