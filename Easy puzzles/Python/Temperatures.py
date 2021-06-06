import sys
import math

n = int(input())  # the number of temperatures to analyse
t_pos=5526
t_neg=-5526
result=0
t_abs_neg=0

for i in input().split():
    t = int(i)
    if t<t_pos and t>0:
        t_pos=t
        t_neg=t_pos+1
    elif t>t_neg and t<0:
        t_neg=t  
    if t_pos<=abs(t_neg):
        result=t_pos
    elif t_pos>abs(t_neg):
        result=t_neg
print(result)