##################################################
### Lecture 05 Exercise 1, 2
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
ex_no = "1"

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
## Initialise variables
##################################################
# NX = 601, c = 15m/s, Δx = 1km, Δt=30 seconds
Nx = 601    # number of space points
Nt = 500    # total time steps
c = 50      # speed of advection
dx = 1000   # distance change within 2 space points
dt = 30     # time change within 2 time steps

# set plotting info
yup = 1.2
ydown = -0.2

##################################################
## Initialise arrays and lists
##################################################
u = np.zeros(Nx)      # current values
u_new = np.zeros(Nx)  # new values

##################################################
## Initialize solution for time level zero
##################################################
# box signal of width 20
u[Nx // 2 - 10:Nx // 2 + 10] = 1.0  

##################################################
## Looping the time steps
##################################################
# calculate sigma
sigma = c * (dt / dx)

# time loop
for n in range(0, Nt + 1):
    # Use F-T B-S scheme
    u_new = ftbs(u, sigma, Nx)

    # set BCs
    # fixed BCs
    u_new[0] = u[0]
    u_new[Nx - 1] = u[Nx - 1]


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
        title_c = "c = " + str(c) + ",  "
        title_n = "n = {:03}".format(n)
        title = title_c + title_n
        plt.title(title, fontsize=15)
        # save figures
        plt.savefig(save_name, dpi=300)

    # update u -> u_new
    u = np.copy(u_new)


##################################################
## The END
##################################################