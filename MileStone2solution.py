#Milestone2
#-----------Importing neccessary libraries
import math
from sympy import symbols, Eq, solve
import numpy as np
import warnings
warnings.filterwarnings('ignore')

#--------Reading Dataset----------
data={}
file =  open("Milestone2\Input\Testcase4.txt","r")
for line in file:
        data[line.rstrip().split(':')[0]]=line.rstrip().split(':')[1]

diameter = int(data['WaferDiameter'])
radius = diameter/2
DieSize_X = int(data['DieSize'].split('x')[0])
DieSize_Y = int(data['DieSize'].split('x')[1])

DieShift1,DieShift2 = list(map(int,data['DieShiftVector'].replace('(','').replace(')','').split(',')))

point1 , point2 =list(map(int,data['ReferenceDie'].replace('(','').replace(')','').split(',')))



start_x = point1 - (DieSize_X/2)
start_y = point2 - (DieSize_Y/2)

print(start_x,start_y)
#BFS
totalBoxes = (math.ceil(diameter/DieSize_X)*math.ceil(diameter/DieSize_Y))
print(totalBoxes)

def isPlaceable(x,y):
    flag = 0

    if((x > radius or x < -radius )and (y > radius or y < -radius)):
        flag += 1
        
    if((x + DieSize_X > radius or x+DieSize_X <- radius) and (y > radius or y<-radius)):
        flag+=1

    if((x>radius or x<-radius) and (y+DieSize_Y>radius or y+DieSize_Y<-radius)):
        flag+=1

    if((x+DieSize_X>radius or x+DieSize_X<-radius) and (y+DieSize_Y>radius or y+DieSize_Y<-radius)):
        flag+=1

    if(flag==4):
        return False
    return True


def BreadthFirstSearch(start_x,start_y):
    queue = []
    Refernce_List = []
    visited = []
    start_x = start_x
    start_y = start_y

    Refernce_List.append([0,0])
    queue.append([start_x,start_y])
    resultant = [(0,0)]
    visited.append((start_x,start_y))


    while(True):
        x , y = queue.pop(0)
        l1 , l2 = Refernce_List.pop(0)
        if(isPlaceable(x,y)==False):
            visited.remove((x,y))
            resultant.remove((l1,l2))
            break
        if((x+DieSize_X,y) not in visited):

            queue.append([x+DieSize_X,y])
            Refernce_List.append([l1+1,l2])

            resultant.append((l1+1,l2))
            visited.append((x+DieSize_X,y))
            
        if((x-DieSize_X,y) not in visited):
            queue.append([x-DieSize_X,y])
            Refernce_List.append([l1-1,l2])

            resultant.append((l1-1,l2))
            visited.append((x-DieSize_X,y))

        if((x,y+DieSize_Y) not in visited):

            queue.append([x,y+DieSize_Y])
            Refernce_List.append([l1,l2+1])

            resultant.append((l1,l2+1))
            visited.append((x,y+DieSize_Y))

        if((x,y-DieSize_Y) not in visited):

            queue.append([x,y-DieSize_Y])
            Refernce_List.append([l1,l2-1])

            resultant.append((l1,l2-1))
            visited.append((x,y-DieSize_Y))

        if((x+DieSize_X,y+DieSize_Y) not in visited):

            queue.append([x+DieSize_X,y+DieSize_Y])
            Refernce_List.append([l1+1,l2+1])

            resultant.append((l1+1,l2+1))
            visited.append((x+DieSize_X,y+DieSize_Y))

        if((x+DieSize_X,y-DieSize_Y) not in visited):

            queue.append([x+DieSize_X,y-DieSize_Y])
            Refernce_List.append([l1+1,l2-1])

            resultant.append((l1+1,l2-1))
            visited.append((x+DieSize_X,y-DieSize_Y))

        if((x-DieSize_X,y-DieSize_Y) not in visited):

            queue.append([x-DieSize_X,y-DieSize_Y])
            Refernce_List.append([l1-1,l2-1])

            resultant.append((l1-1,l2-1))
            visited.append((x-DieSize_X,y-DieSize_Y))

        if((x-DieSize_X,y+DieSize_Y) not in visited):

            queue.append([x-DieSize_X,y+DieSize_Y])
            Refernce_List.append([l1-1,l2+1])

            resultant.append((l1-1,l2+1))
            visited.append((x-DieSize_X,y+DieSize_Y))

        
    return resultant,visited



resultant , visited = BreadthFirstSearch(start_x,start_y)
out = []
for i in range(len(resultant)):
    string = str(resultant[i]).replace(' ', '')+":"+str(visited[i]).replace(' ','')
    out.append(string)

#writing in to the output file
f =  open('OutputMilestone2-4.txt', 'w')
for i in out:
    f.write(i)
    f.write('\n')


#------------------------------------------------------Defingin line equation
"""Angle  = 0
x1,y1 = 0,0
rad = Angle * (math.pi/180)
m = math.tan(rad)

c = 0  #origin

#circle equation

x , y , r = symbols("x,y,r")
eq_circle =  Eq(x**2 + y**2 - Radius**2)
eq_line =  Eq(y -m*x)
pts = solve((eq_circle,eq_line), (x, y))

xst = round(float(pts[0][0]),4)
xend = round(float(pts[1][0]),4)
NumberOfPoints = 10
distances = np.linspace(0,waferDia,NumberOfPoints)
limits = np.linspace(xst,xend,NumberOfPoints)


i = 0
vertical_eqn = []
for i in distances:
    x_val = round(xst + i,4)-Radius
    ystart = round(m * i,4)
    tempy = ystart
    jindex = 0
    index = 
    while(True):
        if(tempy**2 + x_val**2 > Radius**2):
            break
        vertical_eqn.append([(index,jindex)(x_val,tempy)])
        tempy += 30
        jindex += 1
    tempy = ystart
    jindex = 0
    while(True):
        if(tempy**2 + x_val**2 > Radius**2):
            break
        vertical_eqn.append([(index,jindex)(x_val,tempy)])
        tempy -= 30
        jindex -=1
    
for i in vertical_eqn:
    print(i)
print(len(vertical_eqn))
"""





