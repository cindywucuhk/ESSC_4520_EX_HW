##################################################
### Lecture 04 Exercise 3
### Name: Wu Hei Tung
### SID: 1155109536
##################################################
## Import useful packages
##################################################
import numpy as np                # numerical
import matplotlib.pyplot as plt   # plt graph
from PIL import Image             # gif making
import glob                       # gif making
import os                         # dir making
from tabulate import tabulate     # plot table


##################################################
## Declare variables
##################################################
c = 20
Nx = 61
A = 10
dx = 200000
Nn = 20
L = 10 * dx
k = 2 * np.pi / L


##################################################
## Make all the step into a function
##################################################
def Ex3_eq_solving(c, Nx, A, dx, Nn, k, dt, case):
  """ This function include all the steps for
      1 case in Ex3.
  """


  ##################################################
  ## Set plot directory
  ##################################################
  # Directory
  directory = "plt_dt_" + str(dt) + "_" + case
  
  # Parent Directory path
  parent_dir = "Ex/L04/"
  
  # Path
  plot_dir = os.path.join(parent_dir, directory)

  if (os.path.isdir(plot_dir)):
    pass
  else:
    # Create the directory
    os.mkdir(plot_dir)


  ##################################################
  ## create arrays to store the data
  ##################################################
  u = np.zeros(Nx)      # n = n
  u_new = np.zeros(Nx)  # n = n + 1
  u_old = np.zeros(Nx)  # n = n - 1


  ##################################################
  ## Set initial condition
  ##################################################
  for i in range(0,Nx):
    u_old[i] = c + A * np.sin(k*i*dx)

  # plot the figure
  x = range(0, Nx)
  y = u_old
  plt.plot(x,y,color='black')
  fig_name = plot_dir + '/t_0.png'
  up = round(np.max(y)) + 5
  down = round(np.min(y)) - 4
  plt.yticks(range(down,up,2))
  plt.ylabel('u (m/s)')
  plt.xlabel('dx')
  plt.title('n = 0')
  plt.savefig(fig_name)
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
  plt.yticks(range(down,up,2))
  plt.ylabel('u (m/s)')
  plt.xlabel('dx')
  plt.title('n = 1')
  plt.savefig(fig_name)
  plt.close() 
  

  ##################################################
  ## n=1
  ## rmse
  ##################################################
  # analytical solution
  sum_s = np.zeros(Nx)
  omega = k * c
  for i in range(0,Nx):
    u_ana = (1/np.cos(k*i*dx)) * (c + A * np.sin(k*i*dx)) * np.cos(k*i*dx - omega*dt)
  
    sum_s[i] = (u[i] - u_ana)**2

  # rmse
  rmse = [0]
  rmse.append(np.sqrt(np.sum(sum_s)/Nx))
  

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
      
      # rmse
      u_ana = (1/np.cos(k*i*dx)) * (c + A * np.sin(k*i*dx)) * np.cos(k*i*dx - omega*n*dt)
      sum_s[i] = (u_new[i] - u_ana)**2

    # rmse
    rmse.append(np.sqrt(np.sum(sum_s)/Nx))

    # plot the figure
    x = range(0, Nx)
    y = u_new
    plt.plot(x,y,color='black')
    fig_name = plot_dir + '/t_' + str(n) + '.png'
    plt.yticks(range(down,up,2))
    plt.ylabel('u (m/s)')
    plt.xlabel('dx')
    plt.title('n = ' + str(n))
    plt.savefig(fig_name)
    plt.close() 

    # reset u
    u_old = u
    u = u_new


  ##################################################
  ## Plot GIF to show the whole case
  ##################################################
  # Create the frames
  frames = []
  imgs = glob.glob(plot_dir + "/*.png")
  for i in imgs:
      new_frame = Image.open(i)
      frames.append(new_frame)
  
  # Save into a GIF file that loops forever
  frames[0].save(
                (plot_dir + '/' + directory + '.gif'),
                format='GIF',
                append_images=frames[1:],
                save_all=True,
                duration=300, 
                loop=0)

  return rmse


##################################################
## Case that satisfied the CFL condition
## Case 1
##################################################
# decalre dt 
dt = 1000

# set an array to store the rmse
rmse = []
row = []
for n in range(0, Nn+1):
  temp = 'n = ' + str(n)
  row.append(temp)
rmse.append(row)

rmse.append(Ex3_eq_solving(c, Nx, A, dx, Nn, k, dt, '1'))


##################################################
## Case 2
## A = 25m/s, L=10dx
##################################################
# declare case 2
A = 25

rmse.append(Ex3_eq_solving(c, Nx, A, dx, Nn, k, dt, '2'))


##################################################
## Case 2
## A = 10m/s, L=4dx
##################################################
# declare case 2
A = 10
L = 4 * dx
k = 2 * np.pi / L

rmse.append(Ex3_eq_solving(c, Nx, A, dx, Nn, k, dt, '3'))


##################################################
## print table of RMSE
##################################################
col = [' ', 'Case 1 RMS', 'Case 2 RMS', 'Case 3 RMS']
# rearrange rmse
rmse = np.array(rmse).T.tolist()
print(tabulate(rmse, headers=col))


##################################################
## Case that not satisfied the CFL condition
##################################################
# declare dt
dt = 100000

na_rmse = Ex3_eq_solving(c, Nx, A, dx, Nn, k, dt, 'na')


##################################################
## The END
##################################################