##################################################
### Lecture 07 Exercise 2
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
ex_no = "2_3"

# Directory
directory = "Ex" + ex_no

# Parent Directory path
parent_dir = "Ex/L07/"

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
# 3) Open boundary condition
def openbcs(u,uo,un,sigma):
  """ Open boundary condition: un[-1]=uo[-1]-2c(u[-1]-u[-2])
      Argument:
      u[nparray] - 1-D array that needed to fill the bcs
      Return:
      result[nparray] - filled 1-D array
  """
  # copy the array for modification
  result = np.copy(un)
  # add bcs
  result[-1]=uo[-1]-2*sigma*(u[-1]-u[-2])
  
  return result

##################################################
## Initialise variables
##################################################
# NX = 601, c = 15m/s, Δx = 1km, Δt=30 seconds
Nx = 601    # number of space points
Nt = 1201   # total time steps
c = 15      # speed of advection (upwind)
dx = 1000   # distance change within 2 space points
dt = 30     # time change within 2 time steps
rt = 50     # the recoding time step (once in every 30)
met = 'open'     # the method number

# set plotting info
yup = 1
ydown = -1
no_plt = Nt+1    # the first no_plt plot you want to plot (for blow up) 

# filter factor
gamma = 0.2

##################################################
## Initialise arrays and lists
##################################################
u = np.zeros(Nx)      # current values
u_new = np.zeros(Nx)  # new values
u_old = np.zeros(Nx)  # past values
u_fil = np.zeros(Nx)  # diltered values

images = []           # storing ploted images

##################################################
## Open data file for writing model output
##################################################
outfile_name = out_dir + '/L07_ex' + ex_no + '.txt'
outfile = open(outfile_name, 'w')

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
    # set BCs
    # fixed BCs
    if met == 2:
      u = method_2(u)
    elif met == 5:
      u = method_5(u)
    elif met == 'con':
      u[Nx - 1] = u[Nx - 1]
    
    # Use C-T C-S scheme
    u_new = ctcs(u, u_old, sigma, Nx)

    # Open BCs 
    if met == 'open':
      u_new = openbcs(u,u_old,u_new,sigma)
  
    # include a Asselin-Roberts time filter
    # filter
    u_fil = u + gamma * (u_new - 2*u + u_old)
    #u_fil=np.copy(u)
    
    ##################################################
    ## Record outputs
    ##################################################
    if (n % rt) == 0:
        # write the data into a txt file
        u_new.tofile(outfile, sep=',', format='%f')
        outfile.write('\n')

        if (n >= 750):
          # Plot graph in every n%rt == 0
          # plot name
          plt_ex = "/ex" + ex_no + "_"
          fn = "{:03}.png".format(n)
          save_name = out_dir + plt_ex + fn
          print(fn)

          # title name
          if met=='open':
            title_m = "one-way wave equation  "
          else:
            title_m = "Method " + str(met) + ",  "
          title_n = "n = {:03}".format(n)
          title = title_m + title_n
          
          plt.ylim(ydown, yup)
          plt.xlabel("i")
          plt.ylabel("u(m/s)")
          plt.title(title, fontsize=15)
          plt.plot(u_new)
          # save figures
          plt.savefig(save_name, dpi=300)
          plt.close()
          # append the plot to iamges array
          images.append(imageio.imread(save_name))

    # update u -> u_new
    u_old = np.copy(u_fil)
    u = np.copy(u_new)
    


##################################################
## Close file
##################################################
outfile.close() # Close data file


##################################################
## Make GIF
##################################################
gif_name = out_dir + "/L07_ex" + ex_no + ".gif"
imageio.mimsave(gif_name, images, fps=5)


##################################################
## The END
##################################################