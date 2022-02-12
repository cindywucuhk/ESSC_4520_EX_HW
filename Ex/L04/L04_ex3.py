##################################################
### Lecture 04 Exercise 3
### Name: Wu Hei Tung
### SID: 1155109536
##################################################
## Import useful packages
##################################################
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


##################################################
## Set plot directory
##################################################
plot_dir = 'Ex/L04/CFL_plt'


##################################################
## Declare variables that satisfied CFL condition
##################################################
c = 20
Nx = 61
A = 10
dx = 200000
dt = 1000
Nn = 20
L = 10 * dx
k = 2 * np.pi / L


##################################################
## create arrays to store the data
##################################################
u = np.zeros(Nx)      # n = n
u_new = np.zeros(Nx)  # n = n + 1
u_old = np.zeros(Nx)  # n = n - 1

CFL_fig = []          # figures

##################################################
## Set initial condition
##################################################
for i in range(0,Nx):
  u_old[i] = c + A * np.sin(k * i * dx)

# plot the figure
x = range(0, Nx)
y = u_old
plt.plot(x,y,color='black')
fig_name = plot_dir + '/t_0.png'
plt.yticks(range(8,33,2))
plt.title('n = 0')
plt.savefig(fig_name)
#CFL_fig.append(plt.plot(x,y,color='black', animated=True))
plt.close() 

##################################################
## From n=0 to n=1
## use lower order scheme e.g. ftcs
##################################################
for i in range(0,Nx):
  if (i == 0): 
    # apply the boundary conditions at x == 0
    u[i] = u_old[i] - (c*dt/(2*dx)) * (u_old[1] - u_old[i-2])
  elif(i == (Nx-1)):
    # apply the boundary conditions at x == 0
    u[i] = u_old[i] - (c*dt/(2*dx)) * (u_old[1] - u_old[i-1])
  else:
    u[i] = u_old[i] - (c*dt/(2*dx)) * (u_old[i+1] - u_old[i-1])


##################################################
## From n=0 to n=1
## analytical solution
##################################################
# plot the figure
x = range(0, Nx)
y = u
plt.plot(x,y,color='black')
fig_name = plot_dir + '/t_1.png'
plt.yticks(range(8,33,2))
plt.title('n = 1')
plt.savefig(fig_name)
#CFL_fig.append(plt.plot(x,y,color='black', animated=True))
plt.close() 
#rmse

##################################################
## n=2
## using ctcs
##################################################
# time loop
for n in range(2, Nn+1):
  # space loop
  for i in range(0, Nx):
    # apply the boundary conditions
    if (i==(Nx-1)):
      u_new[i] = u_old[i] - (c*dt/(dx)) * (u[1] - u[i-1])
    elif (i==0):
      u_new[i] = u_old[i] - (c*dt/(dx)) * (u[1] - u[i-2])
    else:
      u_new[i] = u_old[i] - (c*dt/(dx)) * (u[i+1] - u[i-1])

  # plot the figure
  x = range(0, Nx)
  y = u_new
  plt.plot(x,y,color='black')
  fig_name = plot_dir + '/t_' + str(n) + '.png'
  plt.yticks(range(8,33,2))
  plt.title('n = ' + str(n))
  plt.savefig(fig_name)
  #CFL_fig.append(plt.plot(x,y,color='black', animated=True))
  plt.close() 

  # reset u
  u_old = u
  u = u_new


from PIL import Image
import glob
 
# Create the frames
frames = []
imgs = glob.glob(plot_dir + "/*.png")
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)
 
# Save into a GIF file that loops forever
frames[0].save((plot_dir + '/CFL_dt_1000.gif'),
               format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=300, loop=0)