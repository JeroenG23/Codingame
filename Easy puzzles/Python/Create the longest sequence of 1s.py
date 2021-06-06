import sys
import math

b = input()
Ones = b.count('1')
Longest_sequence=0
Longest_original_ones=0
Digits_b=[]
Digit_counter=0

for i in range(len(b)):
    Digit_counter+=1
    if i<(len(b)-1):
        if b[i]!=b[i+1]:
            Digits_b.append(Digit_counter)
            Digit_counter=0
    elif i==len(b)-1:
        if b[i]==b[i-1]:
            Digits_b.append(Digit_counter)
        else:
            Digits_b.append(1)

if b[0]=='0':
    for i in range(1, len(Digits_b), 2):
        if Digits_b[i]>Longest_original_ones:
            Longest_original_ones=Digits_b[i]
elif b[0]=='1':
    for i in range(0, len(Digits_b), 2):
        if Digits_b[i]>Longest_original_ones:
            Longest_original_ones=Digits_b[i]

if Ones==0:
    Longest_sequence=0
else:
    Longest_sequence=Longest_original_ones
    if b[0]=='0':
        for i in range(1, len(Digits_b)-2, 2):
            if (Digits_b[i]+Digits_b[i+2]) > Longest_sequence and Digits_b[i+1] ==1:
                Longest_sequence=Digits_b[i]+Digits_b[i+2]    
    elif b[0]=='1':
        for i in range(0, len(Digits_b)-2, 2):
            
            if (Digits_b[i]+Digits_b[i+2]) > Longest_sequence and Digits_b[i+1] ==1:
                Longest_sequence=Digits_b[i]+Digits_b[i+2]
              
print(Longest_sequence+1)