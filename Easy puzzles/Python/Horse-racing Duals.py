import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


Difference_order = ""
Biggest_Value=0
Smallest_Value=0

n = int(input())

List_Horses = [0] * n

for i in range(n):
    pi = int(input())
    List_Horses[i]=pi

Difference=10**10
List_Horses.sort()

   
for i in range(n-1):
    Biggest_Value = (List_Horses)[i+1]
    Smallest_Value = (List_Horses)[i]
    Difference_order = Biggest_Value - Smallest_Value
    if Difference_order < Difference:
        Difference = Difference_order
               

print(Difference)
        
       

        
        






