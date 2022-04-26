##################################################
## L11 Exercise 2
## Name: Wu Hei Tung
## SID: 1155109536
##################################################
## import needed package
##################################################
import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

#################################################
## a) randomly assign masses between 0-1kg as 
##    mass_true
#################################################
m_true = np.array(sorted(np.random.random_sample((100, 1))))
#m_true = np.random.random_sample((100, 1))
print(m_true)

#################################################
## b) create a correct kernel G
#################################################
# set N and M
N = 100
M = 100

# create G
G = np.zeros((N,M))

# assign value for G
for i in range(0,N):
    # the first 2 weight
    if i==0:
        G[i,0]=1
    elif i==1:
        G[i,0]=1
        G[i,1]=1
    else:
        # other case
        G[i,i-2]=1
        G[i,i-1]=1
        G[i,i]=1

print(G)

#################################################
## c) creates synthetic observed data d
#################################################
# create vector of Gaussian random numbers with zero mean and sigma is 0.01 kg
mu = 0          # mean
sigma_d = 0.01    # sigma
n = np.random.normal(mu, sigma_d, size=(100,1))
print(n)

# create d
d = np.matmul(G,m_true) + n
print(d)

#################################################
## d) solves the inverse problem by 
##    simple least squares
#################################################
# Estimated model parameters
Gt = np.transpose(G)
t1 = np.matmul(Gt, G)
t2 = np.matmul(Gt, d)
m_est = np.matmul(la.inv(t1),t2)
dpre = np.matmul(G,m_est)
print("prediction")
print(dpre)

#################################################
## e) plot m_true and m_est
#################################################
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# plot m_true and m est
ax.plot(m_true, color='black', label='$m^{true}$')
ax.plot(m_est, color='red', label='$m^{est}$')
# set legend, xlabel, ylabel, title
ax.legend()
ax.set_ylabel('mass (kg)')
ax.set_xlabel('object')
ax.set_title('True mass and least square mass of 100 objects')

# save figures
fig.savefig('L11_ex2e.png', dpi=300)

#################################################
## f) Counts up the number of estimated model 
##    parameters that are within +-2sigma_m of 
##    their true value
#################################################
# calculate sigma_m
# variance of model parameters
Cm = (sigma_d**2)*la.inv(t1)   
sigma_m = []
for i in range(M):
    # sqrt variance of model parameter
    sigma_m.append(np.sqrt(Cm[i,i])) 

print(sigma_m)

# counts up the number
count_up = np.zeros((100,4))
for i in range(0,M):
    if (m_est[i][0] >= m_true[i][0]-2*sigma_m[i]) & (m_est[i][0] <= m_true[i][0]+2*sigma_m[i]):
        count_up[i,0]=1
    else:
        count_up[i,0]=0

    count_up[i,1]=m_est[i][0]
    count_up[i,2]=mu-2*sigma_m[i]
    count_up[i,3]=mu+2*sigma_m[i]

total_c = np.sum(count_up[:,0])

print(count_up)
print("The number of estimated model parameters that are within +- 2 sigma_m of the true value:")
print(total_c)

#################################################
## g) plot histogram of m_est and m_true
#################################################
# set the size of bin
bin_size = 7
bins_list = np.arange(0,1,1/bin_size)
print(m_true.T)

# plot histogram
figh = plt.figure()
axh = figh.add_subplot(1,1,1)
axh.hist([m_true.T[0],m_est.T[0]],bins_list, rwidth = 0.8,label=['$m^{true}$', '$m^{est}$'])

# set legend, xlabel, ylabel, title
axh.legend()
axh.set_xlabel('mass (kg)')
axh.set_ylabel('number of object')
axh.set_title('Histogram of $m^{true}$ and $m^{est}$')

# save plot
figh.savefig('L11_ex2g.png', dpi=300)


#################################################
### END
#################################################