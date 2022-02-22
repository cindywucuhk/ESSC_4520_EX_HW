##################################################
### Lecture 05 Exercise 4
### Name: Wu Hei Tung
### SID: 1155109536
##################################################
## Import useful packages
##################################################
import numpy as np                # numerical
import matplotlib.pyplot as plt   # plt graph
import os                         # dir making

##################################################
## Set directories
##################################################
# Ex no.
ex_no = "4_1"

# Directory
directory = "Ex" + ex_no

# Parent Directory path
parent_dir = "Ex/L05/"

# Path
out_dir = os.path.join(parent_dir, directory)

if (os.path.isdir(out_dir)):
    pass
else:
    # Create the directory
    os.mkdir(out_dir)


##################################################
## Functions
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
    outp[1:Nx] = inp[1:Nx] - sigma * (inp[1:Nx] - inp[0:Nx - 1])

    return outp


##################################################
#3) C-T C-S
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
## Initialise variables
##################################################
# NX = 601, c = 15m/s, Δx = 1km, Δt=30 seconds
Nx = 601    # number of space points
Nt = 500    # total time steps
c = 15      # speed of advection (upwind)
dx = 1000   # distance change within 2 space points
dt = 30     # time change within 2 time steps

# set plotting info
yup = 1.5
ydown = -0.5

# filter factor
gamma = 0.05

##################################################
## Initialise arrays and lists
##################################################
u = np.zeros(Nx)      # current values
u_new = np.zeros(Nx)  # new values
u_old = np.zeros(Nx)  # past values
u_fil = np.zeros(Nx)  # filtered values

##################################################
## Initialize solution for time level zero
##################################################
# box signal of width 20
u_old[Nx // 2 - 10:Nx // 2 + 10] = 1.0  

##################################################
## Initialize solution for time level 1
##################################################
# calculate sigma
sigma = c * (dt / dx)

# F-T B-S for the first time step
u = ftbs(u_old, sigma, Nx)

##################################################
## Looping the time steps
##################################################
# time loop
for n in range(0, Nt + 1):
    # Use C-T C-S scheme
    u_new = ctcs(u, u_old, sigma, Nx)

    # set BCs
    # fixed BCs
    u_new[0] = u[0]
    u_new[Nx - 1] = u[Nx - 1]

    # filter
    u_fil = u + gamma * (u_new - 2*u + u_old)

    ##################################################
    ## Record outputs
    ##################################################
    # plot name
    plt_ex = "/ex" + ex_no + ".png"
    save_name = out_dir + plt_ex

    if n == 0:
        # plot initial condition
        # plot
        plt.ylim(ydown, yup)
        plt.xlabel("i")
        plt.ylabel("u(m/s)")
        plt.plot(u, linestyle='--', color='black', label='Initial')

    if n == Nt:
        plt.plot(u_new, color='black', label='Numerical')
        plt.legend()
       
        # title name
        title_g = "$\gamma$ = " + str(gamma) + ",  "
        title_c = "c = " + str(c) + ",  "
        title_n = "n = {:03}".format(n)
        title = title_g + title_c + title_n
        plt.title(title, fontsize=15)
        # save figures
        plt.savefig(save_name, dpi=300)


    # update u -> u_new
    u_old = np.copy(u_fil)
    u = np.copy(u_new)
    

##################################################
## The END
##################################################