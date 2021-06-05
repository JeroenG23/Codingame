import sys
import math

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

Grid=[]
for i in range(height):
    Grid.append([""]*width)

for i in range(height):
    row = input() # width characters, each either 0 or .
    for j in range(width):
        Grid[i][j]= row[j]

Grid_Transposed=list(zip(*Grid))
for i in range(height):
    for j in range(width):
        if Grid[i][j]=='0':
            x1 = j 
            y1 = i 
            if j == width-1:
                x2=y2=-1
            else:
                try:
                    x2 = j+1+ Grid[i][j+1:].index('0')
                    y2=i
                except:
                    x2=y2=-1
            if i==height-1:
                x3=y3=-1
            else:
                try:
                    x3 = j
                    y3 = i+1+Grid_Transposed[j][i+1:].index('0')
                except:
                    x3=y3=-1
            print(x1, y1, x2, y2, x3, y3)