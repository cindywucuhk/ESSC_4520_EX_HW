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
## Arguments:
##  inp[nparray] - u
##  inp_o[nparray] - u_old  {for C-S case only}
##  sigma[float] - cdt/dx (or else)
##  Nx[int] - number of space points
## Returns:
##  out[nparray] - u_new
##################################################
# 1) F-T F-S
def ftfs(inp, sigma, Nx):
  """ F-T F-S 
    Arguments:
    inp[nparray] - u
    sigma[float] - cdt/dx (or else)
    Nx[int] - number of space points
    Returns:
    out[nparray] - u_new
  """
  # declare output array
  outp = np.zeros(Nx)
  # calculations
  outp[0:Nx] = inp[0:Nx-1] - sigma*(inp[1:Nx] - inp[0:Nx-1])

  return outp


##################################################
# 2) F-T B-S
def ftbs(inp, sigma, Nx):
  """ F-T B-S 
    Arguments:
    inp[nparray] - u
    sigma[float] - cdt/dx (or else)
    Nx[int] - number of space points
    Returns:
    out[nparray] - u_new
  """
  # declare output array
  outp = np.zeros(Nx)
  # calculations
  outp[1:Nx] = inp[1:Nx] - sigma*(inp[1:Nx]-inp[0:Nx-1])

  return outp


##################################################
# 3) C-T C-S
def ctcs(inp, inp_o, sigma, Nx):
  """ C-T C-S 
    Arguments:
    inp[nparray] - u
    inp_o[nparray] - u_old
    sigma[float] - cdt/dx (or else)
    Nx[int] - number of space points
    Returns:
    out[nparray] - u_new
  """
  # declare output array
  outp = np.zeros(Nx)
  # calculations
  outp[1:Nx-1] = inp_o[1:Nx-1] - sigma*(inp[2:Nx]-inp[0:Nx-2])

  return outp


##################################################