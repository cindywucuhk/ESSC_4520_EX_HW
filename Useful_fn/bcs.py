##################################################
### Different Nummerical Schemes solving 
### the Advection Equation
### Name: Wu Hei Tung
### SID: 1155109536
##################################################
## Import useful packages
##################################################
import numpy as np     # for nummerical munipilation

##################################################
## Functions
##################################################
##  Argument:
##  u[nparray] - 1-D array that needed to fill the bcs
##  Return:
##  result[nparray] - filled 1-D array
##################################################
# 1) Method 2
def method_2(u):
  """ Method 2 computational BCs [u[nx]=u[nx-1]]
      Argument:
      u[nparray] - 1-D array that needed to fill the bcs
      Return:
      result[nparray] - filled 1-D array
  """
  
  # copy the array for modification
  result = np.copy(u)
  # add bcs
  result[-1]=result[-2]
  
  return result

  
##################################################
# 2) Method 5
def method_5(u):
  """ Method 5 computational BCs [u[nx]=2u[nx-1]-u[nx-2]]
      Argument:
      u[nparray] - 1-D array that needed to fill the bcs
      Return:
      result[nparray] - filled 1-D array
  """
  # copy the array for modification
  result = np.copy(u)
  # add bcs
  result[-1] = 2*result[-2]-result[-3]
  
  return result


##################################################