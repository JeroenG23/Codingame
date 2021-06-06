import sys
import math

Matrix = [ [[],[],[]], [[],[],[]], [[],[],[]] ]
Matrix_transposed=[]
Winning_move = False
for i in range(3):
    line = input()
    for j in range(len(line)):
        Matrix[i][j]=line[j]

Dots_quantity=0
Rows_O = []
Rows_X = []
Col_O = []
Col_X = []
Dia_1_9 = []
Dia_3_7 = []
for i in range (len(Matrix)):
    for x in Matrix[i]:
        Dots_quantity_help = Matrix[i].count('.')
        O_quantity= Matrix[i].count('O')
        X_quantity= Matrix[i].count('X')
    Rows_O.append(O_quantity)
    Rows_X.append(X_quantity)
    Dots_quantity = Dots_quantity + Dots_quantity_help 

Matrix_transposed = list(zip(*Matrix) )
for i in range (len(Matrix)):
    for x in Matrix_transposed[i]:
        O_quantity= Matrix_transposed[i].count('O')
        X_quantity= Matrix_transposed[i].count('X')
    Col_O.append(O_quantity)
    Col_X.append(X_quantity)
    Matrix_transposed[i]=list(Matrix_transposed[i])

for i in range(len(Matrix)):
    Counter=0
    for x in Matrix[i]:
        if Counter==i:
            Dia_1_9.append(x)
        Counter+=1
    Counter =0
    for x in Matrix[i]:
        if Counter==2-i:
            Dia_3_7.append(x)
        Counter+=1
O_quantity_dia_1_9 = Dia_1_9.count('O')
X_quantity_dia_1_9 = Dia_1_9.count('X')
O_quantity_dia_3_7 = Dia_3_7.count('O')
X_quantity_dia_3_7 = Dia_3_7.count('X')

Winning_matrix=Matrix
Winning_matrix_transposed=list(Matrix_transposed)
Winning_row=''

if Dots_quantity >= 8:
    Winning_move=False   

for i in range (len(Rows_O)):
    if Rows_O[i]-Rows_X[i]==2:
        Winning_move=True
        for j in range(len(Matrix)):
            for x in Matrix[i]:
                if x=='.':
                    Winning_matrix[i][j]= ('O')
        break
    elif Col_O[i]-Col_X[i]==2:
        Winning_move=True
        for j in range(len(Matrix_transposed)):
            for x in Matrix_transposed[i]:
                if x=='.':
                    Winning_matrix_transposed[i][j]= ('O')
        Winning_matrix=list(zip(*Winning_matrix_transposed))
        break
    elif O_quantity_dia_1_9-X_quantity_dia_1_9==2:
        Winning_move=True
        for j in range (len(Rows_O)):
            if Dia_1_9[j]=='.':
                for x in Matrix[j]:
                    Winning_matrix[j][j]= ('O')
        break
    elif O_quantity_dia_3_7-X_quantity_dia_3_7==2:
        Winning_move=True
        for j in range (len(Rows_O)):
            if Dia_3_7[j]=='.':
                for x in Matrix[j]:
                    Winning_matrix[j][j]= ('O')
        break
    

if Winning_move==True:
    for j in range(len(Winning_matrix)):
        for x in Winning_matrix[j]:
            Winning_row= Winning_row + x
        print(Winning_row[j*3:(j*3)+3])
else:
    print('false')