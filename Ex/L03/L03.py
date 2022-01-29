##################################################
### Lecture 03 Exercise
### Name: Wu Hei Tung
### SID: 1155109536
##################################################
## Import useful packages
##################################################
import numpy as np
#import pandas as pd
from tabulate import tabulate

##################################################
## Exercise 1a
##################################################
# create a function F(x)
def F(a,b,c,d,x):

  output = a*x**3 + b*x**2 + c*x + d

  return output

# set constants
a = 1
b = 2
c = 3
d = 4

# set the change in x
delta_x = [1,0.1,0.01]

# create array to store the result
forward = np.empty(10)
backward = np.empty(10)
center = np.empty(10)
analy = np.empty(10)

# fill the empty array with NaN
forward[:] = np.NaN
backward[:] = np.NaN
center[:] = np.NaN
analy[:] = np.NaN

# assign arbitrary non-zero values to x
x = np.arange(1,11)

# calculate d /dx
for i in range(0,10):
  # numerical method
  forward[i] = (F(a,b,c,d,x[i]+delta_x[0]) - F(a,b,c,d,x[i]))/delta_x[0]
  backward[i] = (F(a,b,c,d,x[i]) - F(a,b,c,d,x[i]-delta_x[0]))/delta_x[0]
  center[i] = (F(a,b,c,d,x[i]+delta_x[0]) - F(a,b,c,d,x[i]-delta_x[0]))/(2*delta_x[0])

  # analytical method
  # dF/dx = 3ax^2 + 2bx + c
  analy[i] = 3*a*x[i]**2 + 2*b*x[i] + c

# numerical - analytical
fordiff = forward - analy
backdiff = backward - analy
cendiff = center - analy

# create header
row = np.empty(11, dtype='object')
row[0] = 'method'
for i in range(1,11):
  name = 'x_'+str(i)
  row[i] = name

# create and print resulted table
table1 = [['forward'],['backward'],['centered']]
for i in range(0,10):
  table1[0].append(fordiff[i])
  table1[1].append(backdiff[i])
  table1[2].append(cendiff[i])
print(tabulate(table1, headers=row))

##################################################
## Exercise 1b
##################################################
# create an array to store the result
F_delta = np.empty(3)
F_delta[:] = np.NaN

# calculate dF/dx
for i in range(0,3):
  # nummerical
  F_delta[i] = (F(a,b,c,d,x[0]+delta_x[i]) - F(a,b,c,d,x[i]-delta_x[i]))/(2*delta_x[i])

  # analytical
  analy_delta = 3*a*x[0]**2 + 2*b*x[0] + c

# find different 
F_delt_diff = F_delta - analy_delta

# create heading
row = np.empty(4, dtype='object')
row[0] = ' '
for i in range(1,4):
  name = '(\u0394x)_'+str(i)
  row[i] = name

# create and print resulted table
table2 = [['\u0394x'],['dF/dx']]
for i in range(0,3):
  table2[0].append(delta_x[i])
  table2[1].append(round(F_delt_diff[i],4-int(np.floor(np.log10(np.absolute(F_delt_diff[i]))))-1))

print(tabulate(table2, headers=row))