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
RH0=0.8
c=np.zeros(1000)
RH=np.arange(0,120,0.12)/100
print(len(RH))

for i in range(0,1000):
  if RH[i]<=RH0:
    c[i]=0
  elif RH[i]>=1:
    c[i]=1
  else:
    c[i]=((RH[i]-RH0)/(1-RH[i]))**2
print(RH)
print(c)
c[c>1]=1
no=np.where(RH<=RH0)
always=np.where(RH>=1)
some=np.where((RH>RH0)&(RH<1))

#################################################
## Plot the c vs RH
#################################################
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
c_plot = ax.plot(RH[some], c[some], color='black')
c_plot1 = ax.plot(RH[no], c[no], color='black')
c_plot2 = ax.plot(RH[always], c[always], color='black')
ax.set_xlabel('RH (%)')
ax.set_ylabel('c (%)')
fig.savefig('L08_ex1')