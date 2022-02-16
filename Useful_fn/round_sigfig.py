##################################################
### Round to i significant figures
### Name: Wu Hei Tung
### SID: 1155109536
##################################################
## Import useful packages
##################################################
import numpy as np     # for nummerical munipilation


##################################################
## Functions
##################################################
# round to significant figures
def sigfig(x, i):
  """ This function is used to round a value to a significant figures
    Arguments:
    x[float] - The number to round
    i[int] - The number of sugnificant values for rounding
    Return:
    r[float] - The rounded number
  """

  r = round(x,i-int(np.floor(np.log10(np.absolute(x))))-1)

  return r


##################################################