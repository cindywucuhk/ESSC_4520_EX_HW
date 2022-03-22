##################################################
### Lecture 08 Exercise 1
### Name: Wu Hei Tung
### SID: 1155109536
##################################################
## Import useful package
##################################################
import numpy as np
import matplotlib.pyplot as plt

##################################################
## make a plot array
##################################################
RH0=0.8                             # critical RH0
c=np.zeros(1000)                    # subgrid scale cloud coverage
RH=np.arange(0,150,0.15)/100        # resolved scale RH

for i in range(0,1000):

  if RH[i]<=RH0:                    # RH <= RH0
    c[i]=0
  elif RH[i]>=1:                    # RH => 100%
    c[i]=1
  else:                             # RH0 < RH < 100
    c[i]=((RH[i]-RH0)/(1-RH0))**2


#################################################
## Plot the c vs RH
#################################################
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
c_plot = ax.plot(RH*100, c*100, color='black')
ax.set_xlabel('RH (%)')
ax.set_ylabel('C (%)')
ax.set_title('Parameterized C vs Resolved RH')
fig.savefig('L08_ex1')