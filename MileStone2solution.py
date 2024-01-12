#Milestone2
#-----------Importing neccessary libraries
import math
from sympy import symbols, Eq, solve
import numpy as np

#--------Reading Dataset----------

file = open("Milestone2\Input\Testcase1.txt",'r')
waferDia = int(file.readline().split(':')[1])
Diesize = file.readline().split(':')[1]
Dieshiftvector = file.readline().split(':')[1]
Reference = file.readline().split(':')[1]
file.close()

