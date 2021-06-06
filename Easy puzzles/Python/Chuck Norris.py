import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

Binary_list=[]
First_unary=""
Second_unary=""
Solution_unary=""

for i in range( len(message)):
    Number = ord(message[i])
    Binary_with_b = bin(Number)
    Binary = Binary_with_b[2:]
    Binary= Binary.zfill(7)
    Binary_list.append(Binary)

Binary_message = ''.join(Binary_list)
Counter_0 = 0
Counter_1 = 0

i=0
while i != (len(Binary_message)):

    Second_unary= "0"

    if Binary_message [i]=="0" and Counter_0==0:
        Counter_1=0
        First_unary=" 00 "
        Counter_0+=1

    elif Binary_message [i]=="1" and Counter_1==0:
        Counter_0=0
        First_unary=" 0 "
        Counter_1+=1

    elif Binary_message [i]=="0" and Counter_0>=1:
        First_unary=""
        Counter_0+=1

    elif Binary_message [i]=="1" and Counter_1>=1:
        First_unary=""
        Counter_1+=1

    
    Solution_unary = Solution_unary + First_unary + Second_unary

    
    i+=1


# Write an answer using print
#print("Debug messages...", file=sys.stderr, flush=True)

print(Solution_unary.lstrip())
