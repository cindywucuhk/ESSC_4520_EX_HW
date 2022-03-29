##################################################
## L09 Exercise 2
## Name: Wu Hei Tung
## SID: 1155109536
## * This code is modified from  "Script to 
##   integrate "chaotic" Lorenz 3-component system"
##################################################
## Import packages
##################################################
import numpy as np                # numerical
import matplotlib.pyplot as plt   # plt graph
import imageio                    # plt gif
import os                         # dir making


##################################################
## Set directories
##################################################
# Parent Directory path
parent_dir = "Ex/L09/"


##################################################
## Script to integrate "chaotic" Lorenz 
## 3-component system
##################################################
# Initialize X,Y,Z
X0,Y0,Z0 = 10., 0., 0.
V = np.array([X0, Y0, Z0])
# constants
r, sig, b = 28., 10., 8/3.
dt = 0.01
time = 100
# Counter n
n = 0

# Initialize the variables
mylist = np.arange(0,time+dt,dt)
dimsize = len(mylist)
zarr = np.zeros(dimsize)
xp,yp,zp,thist = np.copy(zarr),np.copy(zarr),np.copy(zarr),np.copy(zarr)

# the first calculated numbers are in xp[0], yp[0], zp[0]
for t in mylist:
  # get rid of precision issue of arange
  t = int(t*100)/100.
  dXdt = sig*(V[1] - V[0])
  dYdt = r*V[0] - V[1] - V[0]*V[2]
  dZdt = V[0]*V[1] - b*V[2]
  V[0] = V[0] + (dXdt * dt)
  V[1] = V[1] + (dYdt * dt)
  V[2] = V[2] + (dZdt * dt)
  xp[n],yp[n],zp[n] = V[0], V[1], V[2]
  thist[n] = t
  n += 1
          

##################################################
## L09 Ex2a
## Draw the time series of the X, Y, Z in the 
## same graph with time from 0 to 100.
##################################################
# set save name
save_name = 'L09_ex2a.png'
# title name
title = 'Time series '
# plot figure
fig = plt.figure()
ax = fig.add_subplot(111)
# plot
ax.plot(mylist, xp, label='X')
ax.plot(mylist, yp, label='Y')
ax.plot(mylist, zp, label='Z')
ax.legend()                         # set legend
ax.set_xlabel('timestep t')         # set xlabel
ax.set_title(title, fontsize=15)    # set title
# save figure
fig.savefig((save_name), dpi=300)


##################################################
## L09 Ex2b
## Use the script to write a function that will 
## need the initial conditions (X0, Y0, Z0) as 
## the inputs.
##################################################
def Lorenz_model(X0, Y0, Z0):
  """ This model output the Lorenz model with setted initial condition.
    Arguments:
      X0 - initial X
      Y0 - initial Y
      Z0 - initial Z
    Returns:
      xp - array of X
      yp - array of Y
      zp - array of Z
      thist - array of time step
  """
  V = np.array([X0, Y0, Z0])
  # constants
  r, sig, b = 28., 10., 8/3.
  dt = 0.01
  time = 100
  # Counter n
  n = 0
  
  # Initialize the variables
  mylist = np.arange(0,time+dt,dt)
  dimsize = len(mylist)
  zarr = np.zeros(dimsize)
  xp,yp,zp,thist = np.copy(zarr),np.copy(zarr),np.copy(zarr),np.copy(zarr)
  
  # the first calculated numbers are in xp[0], yp[0], zp[0]
  for t in mylist:
    # get rid of precision issue of arange
    t = int(t*100)/100.
    dXdt = sig*(V[1] - V[0])
    dYdt = r*V[0] - V[1] - V[0]*V[2]
    dZdt = V[0]*V[1] - b*V[2]
    V[0] = V[0] + (dXdt * dt)
    V[1] = V[1] + (dYdt * dt)
    V[2] = V[2] + (dZdt * dt)
    xp[n],yp[n],zp[n] = V[0], V[1], V[2]
    thist[n] = t
    n += 1

  return xp, yp, zp, thist

# call fn
xi, yi, zi, thisti = Lorenz_model(10.0, 0, 0)
xii, yii, zii, thistii = Lorenz_model(10+0.001, 0, 0)
xiii, yiii, ziii, thistiii = Lorenz_model(10-0.001, 0, 0)

# set save name
save_name = 'L09_ex2b.png'
# title name
title = 'Time series of X'
# plot figure
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(mylist, xi, label='(X0, Y0, Z0) = (10, 0, 0)')
ax.plot(mylist, xii, label='(X0, Y0, Z0) = (10+0.001, 0, 0)')
ax.plot(mylist, xiii, label='(X0, Y0, Z0) = (10-0.001, 0, 0)')
ax.legend()                         # set legend    
ax.set_xlabel('timestep t')         # set xlabel    
ax.set_title(title, fontsize=15)    # set title
# save figure
fig.savefig((parent_dir+save_name), dpi=300)


##################################################
## L09 Ex2c
## Modified the script so that a constant forcing 
## F is included on the right side of the equation dX/dt
##################################################
def Lorenz_model_M(X0, Y0, Z0, F):
  """ This model output the Lorenz model with setted initial condition.
    Arguments:
      X0 - initial X
      Y0 - initial Y
      Z0 - initial Z
      F - constant forcing
    Returns:
      xp - array of X
      yp - array of Y
      zp - array of Z
      thist - array of time step
  """
  V = np.array([X0, Y0, Z0])
  # constants
  r, sig, b = 28., 10., 8/3.
  dt = 0.01
  time = 100
  # Counter n
  n = 0
  
  # Initialize the variables
  mylist = np.arange(0,time+dt,dt)
  dimsize = len(mylist)
  zarr = np.zeros(dimsize)
  xp,yp,zp,thist = np.copy(zarr),np.copy(zarr),np.copy(zarr),np.copy(zarr)
  
  # the first calculated numbers are in xp[0], yp[0], zp[0]
  for t in mylist:
    # get rid of precision issue of arange
    t = int(t*100)/100.
    dXdt = sig*(V[1] - V[0]) + F
    dYdt = r*V[0] - V[1] - V[0]*V[2]
    dZdt = V[0]*V[1] - b*V[2]
    V[0] = V[0] + (dXdt * dt)
    V[1] = V[1] + (dYdt * dt)
    V[2] = V[2] + (dZdt * dt)
    xp[n],yp[n],zp[n] = V[0], V[1], V[2]
    thist[n] = t
    n += 1

  return xp, yp, zp, thist

# call fns
# experiment set 1 F=0
xia, yia, zia, thistia = Lorenz_model_M(10.0, 0, 0, 0)
xiia, yiia, ziia, thistiia = Lorenz_model_M(10+0.001, 0, 0, 0)
xiiia, yiiia, ziiia, thistiiia = Lorenz_model_M(10-0.001, 0, 0, 0)

# experiment set 2 F=10
xib, yib, zib, thistib = Lorenz_model_M(10.0, 0, 0, 10)
xiib, yiib, ziib, thistiib = Lorenz_model_M(10+0.001, 0, 0, 10)
xiiib, yiiib, ziiib, thistiiib = Lorenz_model_M(10-0.001, 0, 0, 10)

# set save name
save_name = 'L09_ex2c_1.png'
# title name
title = 'Time series of X (F = 0)'
# plot figure
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(mylist, xia, label='(X0, Y0, Z0) = (10, 0, 0)')
ax.plot(mylist, xiia, label='(X0, Y0, Z0) = (10+0.001, 0, 0)')
ax.plot(mylist, xiiia, label='(X0, Y0, Z0) = (10-0.001, 0, 0)')
ax.legend()                         # set legend    
ax.set_xlabel('timestep t')         # set xlabel
ax.set_title(title, fontsize=15)    # set title
# save figure
fig.savefig((parent_dir+save_name), dpi=300)

# set save name
save_name = 'L09_ex2c_2.png'
# title name
title = 'Time series of X (F = 10)'
# plot figure
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(mylist, xib, label='(X0, Y0, Z0) = (10, 0, 0)')
ax.plot(mylist, xiib, label='(X0, Y0, Z0) = (10+0.001, 0, 0)')
ax.plot(mylist, xiiib, label='(X0, Y0, Z0) = (10-0.001, 0, 0)')
ax.legend()                         # set legend
ax.set_xlabel('timestep t')         # set xlabel
ax.set_title(title, fontsize=15)    # title
# save figure
fig.savefig((parent_dir+save_name), dpi=300)


##################################################
## L09 Ex2d
## Use Adam-Bashforth Scheme
##################################################
def Lorenz_model_A(X0, Y0, Z0):
  """ This model output the Lorenz model with setted initial condition. Using third-order Adams-Bashforth scheme.
    Arguments:
      X0 - initial X
      Y0 - initial Y
      Z0 - initial Z
    Returns:
      xp - array of X
      yp - array of Y
      zp - array of Z
      thist - array of time step
  """
  # set list V storing X, Y and Z
  V = [[X0], [Y0], [Z0]]
  # constants
  r, sig, b = 28., 10., 8/3.
  dt = 0.01
  time = 100
  # Counter n
  n = 0
  
  # Initialize the variables
  mylist = np.arange(0,time+dt,dt)
  dimsize = len(mylist)
  zarr = np.zeros(dimsize)
  xp,yp,zp,thist = np.copy(zarr),np.copy(zarr),np.copy(zarr),np.copy(zarr)
  
  # the first calculated numbers are in xp[0], yp[0], zp[0]
  for t in mylist:
    # get rid of precision issue of arange
    t = int(t*100)/100.

    # third-order Adams-Bashforth scheme
    # set X, Y, Z and dXdt, dYdt, dZdt in n=0, n=1, n=2
    if n <= 2:
      # dXdt, dYdt, dZdt in n=0, n=1, n=2
      dXdt = sig*(V[1][n] - V[0][n])
      dYdt = r*V[0][n] - V[1][n] - V[0][n]*V[2][n]
      dZdt = V[0][n]*V[1][n] - b*V[2][n]
      # set X, Y, Z in n=0, n=1, n=2
      V[0].append(V[0][n] + (dXdt * dt))    # X
      V[1].append(V[1][n] + (dYdt * dt))    # Y
      V[2].append(V[2][n] + (dZdt * dt))    # Z
      # Store the result in xp, yp, zp
      xp[n],yp[n],zp[n] = V[0][n], V[1][n], V[2][n]
    else:
      # create 3 list to store the dXdt, dYdt, dZdt in n>2  
      dXdt = []
      dYdt = []
      dZdt = []
      # calculate Gn, Gn-1, Gn-2
      for i in range(0,3):
        dXdt.append(sig*(V[1][i] - V[0][i]))
        dYdt.append(r*V[0][i] - V[1][i] - V[0][i]*V[2][i])
        dZdt.append(V[0][i]*V[1][i] - b*V[2][i])
      # update X, Y and Z in n-2, n-1
      for i in range(0,2):
          V[0][i] = V[0][i+1]
          V[1][i] = V[1][i+1]
          V[2][i] = V[2][i+1]
      # calculate new X, Y, Z in n
      V[0][2] = V[0][2] + (dt/12) * (23*dXdt[2] - 16*dXdt[1] + 5*dXdt[0])
      V[1][2] = V[1][2] + (dt/12) * (23*dYdt[2] - 16*dYdt[1] + 5*dYdt[0])
      V[2][2] = V[2][2] + (dt/12) * (23*dZdt[2] - 16*dZdt[1] + 5*dZdt[0])
      # store the result in xp, yp, zp
      xp[n],yp[n],zp[n] = V[0][2], V[1][2], V[2][2]

    # store timesteps array
    thist[n] = t
    n += 1

  return xp, yp, zp, thist

# call fn
xi, yi, zi, thisti = Lorenz_model_A(10.0, 0, 0)
xii, yii, zii, thistii = Lorenz_model_A(10+0.001, 0, 0)
xiii, yiii, ziii, thistiii = Lorenz_model_A(10-0.001, 0, 0)

# set save name
save_name = 'L09_ex2d.png'
# title name
title = 'Time series of X'
# plot figure
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(mylist, xi, label='(X0, Y0, Z0) = (10, 0, 0)')
ax.plot(mylist, xii, label='(X0, Y0, Z0) = (10+0.001, 0, 0)')
ax.plot(mylist, xiii, label='(X0, Y0, Z0) = (10-0.001, 0, 0)')
ax.legend()                         # set legend
ax.set_xlabel('timestep t')         # set xlabel
ax.set_title(title, fontsize=15)    # set title
# save figure
fig.savefig((parent_dir+save_name), dpi=300)



##################################################
## L09 Ex2e
## Trajectory of Lorenz Model and sensitivity to 
## initial condition
##################################################
# plot 3d trajectory of Lorenz Model in xyz plane
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(xia, yia, zia, lw=0.5, label='(X0, Y0, Z0) = (10, 0, 0)')
ax.plot(xiia, yiia, ziia, lw=0.5, label='(X0, Y0, Z0) = (10+0.001, 0, 0)')
ax.plot(xiiia, yiiia, ziiia, lw=0.5, label='(X0, Y0, Z0) = (10-0.001, 0, 0)')
ax.legend()                                         # set legend
ax.set_title('Trajectory of the Lorenz Model')      # set title
# save figure
fig.savefig(parent_dir + 'L09_ex2e.png')


##################################################
## The END
##################################################