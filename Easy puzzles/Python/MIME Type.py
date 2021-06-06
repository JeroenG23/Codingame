import sys
import math

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

Association_table = {}
for i in range(n):
    ext, mt = input().split()  # ext: file extension, mt: MIME type.
    Association_table[ext.upper()]= mt

for i in range(q):
    fname = input().split(".")  # One file name per line.  
    if len(fname)>1:
        print(Association_table.get(fname[-1].upper(),"UNKNOWN")) # For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
    else: 
        print("UNKNOWN")
