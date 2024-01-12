#Milestone1
#-----------Importing neccessary libraries
import math
from sympy import symbols, Eq, solve
import numpy as np

#--------Reading Dataset----------

file = open("KLA-Hackathon\Milestone1\Input\Testcase1.txt",'r')
waferDia = int(file.readline().split(':')[1])
radius = waferDia/2
NumberOfPoints = int(file.readline().split(':')[1])
Angle = int(file.readline().split(':')[1])
file.close()
print(waferDia,NumberOfPoints,Angle)

#---To find the line segment y = mx +c
x1,y1 = 0,0
rad = Angle * (math.pi/180)
m = math.tan(rad)
c = 0  #origin

#circle equation

x , y , r = symbols("x,y,r")

eq_circle =  Eq(x**2 + y**2 - radius**2)
eq_line =  Eq(y -m*x)

pts = solve((eq_circle,eq_line), (x, y))

xst = round(float(pts[0][0]),4)
xend = round(float(pts[1][0]),4)
print(xst,xend)

distances = np.linspace(0,waferDia,NumberOfPoints)
limits = np.linspace(xst,xend,NumberOfPoints)


j = 0

outfile = open("Output_Milestone1.txt","w")


for i in limits:
    if(m == 0):
        outfile.write("("+str(round(0.0))+", "+ str(round(xst + distances[j],4))+")\n")
    else:
        outfile.write("("+str(round(m * i,4))+", "+ str(round(xst + distances[j],4))+")\n")
    j += 1
outfile.close()