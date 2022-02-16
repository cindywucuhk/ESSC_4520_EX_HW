##################################################
### Lecture 05 Exercise 1, 2
### Name: Wu Hei Tung
### SID: 1155109536
##################################################
## Import useful packages
##################################################
import numpy as np                # numerical
import matplotlib.pyplot as plt   # plt graph
import imageio                    # plt gif
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
c = 15      # speed of advection (upwind)
dx = 1000   # distance change within 2 space points
dt = 30     # time change within 2 time steps
rt = 30     # the recoding time step (once in every 30)

# set plotting info
yup = 1.2
ydown = -0.2
no_plt = Nt+1    # the first no_plt plot you want to plot (for blow up) 

##################################################
## Initialise arrays and lists
##################################################
u = np.zeros(Nx)      # current values
u_new = np.zeros(Nx)  # new values

images = []           # storing ploted images

##################################################
## Open data file for writing model output
##################################################
outfile_name = out_dir + '/L05_ex' + ex_no + '.txt'
outfile = open(outfile_name, 'w')

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
    if (n % rt) == 0:
        # write the data into a txt file
        u_new.tofile(outfile, sep=',', format='%f')
        outfile.write('\n')

        if n < no_plt:
          # Plot graph in every n%rt == 0
          # plot name
          plt_ex = "/ex" + ex_no + "_"
          fn = "{:03}.png".format(n)
          save_name = out_dir + plt_ex + fn
          print(fn)

          # title name
          title_c = "c = " + str(c) + ",  "
          title_n = "n = {:03}".format(n)
          title = title_c + title_n
          
          plt.ylim(ydown, yup)
          plt.xlabel("i")
          plt.ylabel("u(m/s)")
          plt.title(title, fontsize=15)
          plt.plot(u)
          # save figures
          plt.savefig(save_name, dpi=300)
          # append the plot to iamges array
          images.append(imageio.imread(save_name))

    # update u -> u_new
    u = np.copy(u_new)


##################################################
## Close file
##################################################
outfile.close() # Close data file


##################################################
## Make GIF
##################################################
gif_name = out_dir + "/L05_ex" + ex_no + ".gif"
imageio.mimsave(gif_name, images, fps=5)


##################################################
## The END
##################################################