import sys
import math
import operator

score =0
Dictionary = {}
size = int(input())
n = int(input())
for i in range(n):
    name = input()
    Dictionary.update({name:score})
t = int(input())
for i in range(t):
    inputs = input().split()
    throw_name = inputs[0]
    throw_x = int(inputs[1])
    throw_y = int(inputs[2])
    score=0
    if math.fabs(throw_x) <= size/2 and math.fabs(throw_y) <=size/2:
        score = 5
        if throw_x*throw_x + throw_y*throw_y <= (size/2)*(size/2):
            score = 10
            if (math.fabs(throw_x) + math.fabs(throw_y)) <= size/2:
                score = 15
    Dictionary[throw_name]=Dictionary[throw_name]+score
Sorted_Dictionary=sorted(Dictionary.items(), key=operator.itemgetter(1), reverse=True)

for i in range(n):
    print(Sorted_Dictionary[i][0], Sorted_Dictionary[i][1])