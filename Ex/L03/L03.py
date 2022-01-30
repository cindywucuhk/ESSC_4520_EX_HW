##################################################
### Lecture 03 Exercise
### Name: Wu Hei Tung
### SID: 1155109536
##################################################
## Import useful packages
##################################################
import numpy as np
from tabulate import tabulate


##################################################
## Functions
##################################################
# round to significant figures
def sigfig(x, i):

  r = round(x,i-int(np.floor(np.log10(np.absolute(x))))-1)

  return r


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
  name = 'x_'+str(i) + '=' + str(x[i-1])
  row[i] = name

# create and print resulted table
table1 = [['forward'],['backward'],['centered']]
for i in range(0,10):
  table1[0].append(sigfig(fordiff[i],4))
  table1[1].append(sigfig(backdiff[i],4))
  table1[2].append(sigfig(cendiff[i],4))
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
  F_delta[i] = (F(a,b,c,d,x[0]+delta_x[i]) - F(a,b,c,d,x[0]-delta_x[i]))/(2*delta_x[i])
  
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
  table2[1].append(sigfig(F_delt_diff[i],4))

# print the result in a table
print(tabulate(table2, headers=row))



##################################################
## Exercise 2
##################################################
# function
def F2(a,b,c,x):

  output = a*x**2 + b*x + c

  return output

# assign a, b, c to non-zero value
a = 1
b = 2 
c = 3

# assign 10 arbitrary values for x
x = np.arange(10,21)

# assign 3 delta x
delta_x = [3,2,1]

dfdx=[['\u0394x=' + str(delta_x[0])], ['\u0394x=' + str(delta_x[1])], ['\u0394x=' + str(delta_x[2])], ['analytical'], ['\u0394(\u0394x=' + str(delta_x[0])+')'], ['\u0394(\u0394x=' + str(delta_x[1])+')'], ['\u0394(\u0394x=' + str(delta_x[2])+')']]

# calculate dF/dx
for i in range(0,11):
  # analytical result
  analytical = 2*a*x[i] + b
  dfdx[3].append(sigfig(analytical,4))
  for j in range(0,3):
    # nummerical results
    nummerical = (F2(a,b,c,x[i]+delta_x[j]) - F2(a,b,c,x[i]-delta_x[j]))/(2*delta_x[j])
    dfdx[j].append(sigfig(nummerical,4))

    # nummerical-analytical
    diff = nummerical - analytical
    
    if (diff != 0):
      dfdx[j+4].append(sigfig(diff,4))
    else:
      dfdx[j+4].append(diff)

# create heading of table
heading = np.empty(11, dtype='object')
heading[0] = ' '
for i in range(1,11):
  heading[i] = 'x_' + str(i) + '=' + str(x[i-1])

# print the results in a table
print(tabulate(dfdx, headers=heading))



##################################################
## Exercise 3a
##################################################
# create function
def F3(x):

  output = 400 * np.cos(np.pi*x/16)

  return output

# set x and delta x
x = 3
delta_x = 1

# set a list to store all the results
result_ex3a = [['dF/dx'],['absolute error']]

# calculate the result
result = []
# analytical
result.append(-25 * np.pi * np.sin(np.pi*x/16))
# forward
result.append((F3(x+delta_x) - F3(x))/(delta_x))
# backward
result.append((F3(x) - F3(x-delta_x))/(delta_x))
# centered
result.append((F3(x+delta_x) - F3(x-delta_x))/(2*delta_x))
# 4th-order
result.append((4/3)*((F3(x+delta_x) - F3(x-delta_x))/(2*delta_x)) - (1/3)*((F3(x+2*delta_x) - F3(x-2*delta_x))/(4*delta_x)))

# store all the results in a list
# store analytical result
result_ex3a[0].append(sigfig(result[0],4))
result_ex3a[1].append(0)
for i in range(1,5):
  # store nummerical results
  result_ex3a[0].append(sigfig(result[i],4))
  # store absolute errors
  result_ex3a[1].append(sigfig(result[i]-result[0],4))

# create heading 
heading = ['analytical','forward','backward','centered','4th-order']

# print the results in a table
print(tabulate(result_ex3a, headers=heading))



##################################################
## Exercise 3b
##################################################
# set a list to store all the results
result_ex3b = [['d^2F/dx^2'],['absolute error']]

# calculate the result
result = []
# analytical
result.append((-25/16)*((np.pi)**2)*np.cos(np.pi*x/16))
# 2nd-order
result.append((F3(x+delta_x)+F3(x-delta_x)-2*F3(x))/((delta_x)**2))
# 4th-order
result.append((1/((delta_x)**2))*((4/3)*(F3(x+delta_x)+F3(x-delta_x))-((1/12)*(F3(x+2*delta_x)+F3(x-2*delta_x)))-((5/2)*(F3(x)))))

# store all the results in a list
# store analytical result
result_ex3b[0].append(sigfig(result[0],4))
result_ex3b[1].append(0)
for i in range(1,3):
  # store nummerical results
  result_ex3b[0].append(sigfig(result[i],4))
  # store absolute errors
  result_ex3b[1].append(sigfig(result[i]-result[0],4))

# create heading 
heading = ['analytical','2nd-order','4th-order']

# print the results in a table
print(tabulate(result_ex3b, headers=heading))



##################################################
## THE END
##################################################