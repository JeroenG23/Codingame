import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
width, height = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
Jump_list=[]
Jump_list.append([x0,y0])
i=0
x=x0
y=y0
Distance_x = Distance_y = 0
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    i+=1
    Distance_R = (width-1-x)//2
    Distance_L = x//2
    Distance_D = (height-1-y)//2
    Distance_U = y//2

    if 'R' in bomb_dir:
        if Distance_x==0:
            Distance_x = Distance_R
        x= x+Distance_x

    if 'L' in bomb_dir:
        if Distance_x==0:
            Distance_x = Distance_L
        x=x-Distance_x
        
    if 'D' in bomb_dir:
        if Distance_y==0:
            Distance_y = Distance_D
        y=y+Distance_y
        
    if 'U' in bomb_dir:
        if Distance_y==0:
            Distance_y = Distance_U
        y=y-Distance_y
    if Distance_x<=1:
        Distance_x=1     
    else:
        Distance_x=((Distance_x+1)//2)
    if Distance_y<=1:
        Distance_y=1
    else:
        Distance_y=((Distance_y+1)//2)
    print(x, y)
    #print("Debug messages...", file=sys.stderr, flush=True)