import sys
import math

l = int(input())
h = int(input())
t = input()
t = t.upper()

ArtArray = []
RefArray = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "?"]
Solving_Index_Array = []
Solution_Row = str("")

#Filling up array ASCII Art. Array of 5 rows, each row is a list of 27 (ABC+?) lists of 4 elements.
for i in range(h):
    row = list(input())
    Art_row = [row[i:i + l] for i in range(0,len(row),l)]
    ArtArray.append(Art_row)
      
#Filling up Solving Array by index of RefArray (alphabet)
for elem in t:
    try:
        Solving_Index = RefArray.index(elem)
    except ValueError:
        Solving_Index = 26
    Solving_Index_Array.append(Solving_Index)
    
#Printing solution: z for the 4 elements of list, y for the 27 lists, x for the rows
for x in range(h):
    for y in range(len(Solving_Index_Array)):
        y_index=Solving_Index_Array[y]
        for z in range(l):
            Solution_Row = Solution_Row + ArtArray[x][y_index][z]
    Solution = Solution_Row
    Solution_Row = ""        
    print(Solution)  



