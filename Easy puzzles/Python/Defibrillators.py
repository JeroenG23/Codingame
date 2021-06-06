import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = float(input().replace(",","."))*math.pi/180
lat = float(input().replace(",","."))*math.pi/180
n = int(input())
defib=[]
for i in range(n):
    defib.append(input().split(";"))

Closest_d=10**10
for i in range(len(defib)):
    x = (lon - float(defib[i][4].replace(",","."))*math.pi/180)*math.cos(0.5*(lat+float(defib[i][5].replace(",","."))*math.pi/180))
    y = lat-float(defib[i][5].replace(",","."))*math.pi/180
    d = math.sqrt( x*x + y*y )*6371
    if d<Closest_d:
        Closest_d=d
        Closest_defib=i

print(defib[Closest_defib][1])