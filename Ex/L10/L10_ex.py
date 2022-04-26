#################################################
### Lecture 10 Exercise 1
### Name: Wu Hei Tung
### SID: 1155109536
#################################################
## Importing
#################################################
# import useful package
import numpy as np
import matplotlib.pyplot as plt
import math

#################################################
## Setting
#################################################
# set initial concentration
con_O30 = 0
con_O0 = 0
con_NO0 = 10**12
con_NO20 = 10**10

# set variables
h = 10          # Time step (s)
T = 298         # Temperature (K)
Np = 200        # Consecutive iterations

# set coefficients
k1 = (1.4e3)*math.exp(1175/T)
k2 = (1.8e-12)*math.exp(-1370/T)
J = 1.7e-2

# set list to store data
con_O3 = [con_O30]
con_NO2 = [con_NO20]
con_NO = [con_NO0]
con_O = [con_O0]

#################################################
## Solve chemical ODEs using MIE algorithm
#################################################
# Functions
# 1) Backward Euler Concentration
def Back_Euler(m_con, P_B_m, V_B_m, h):
    """ Backward Euler Concentration
    Arguments:
    m_con - Concentration of the target species at iteration m (N[i,B,m])
    P_B_m - Production rate of the target species (BE)
    V_B_m - Loss rate/m1_con of the target species (BE)
    h - timestep
    Returns:
    m1_con - Concentration of the target species at iteration m+1 (N[i,B,m+1])
    """

    m1_con = (m_con + h*P_B_m)/(1+h*V_B_m)

    return m1_con

# 2) Foreward Euler Concentration
def Fore_Euler(m_con, P_B_m, L_B_m, h):
    """ Backward Euler Concentration
    Arguments:
    m_con - Concentration of the target species at iteration m (N[i,F,m])
    P_B_m - Production rate of the target species (BE)
    L_B_m - Loss rate of the target species (BE)
    h - timestep
    Returns:
    m1_con - Concentration of the target species at iteration m+1 (N[i,B,m+1])
    """

    m1_con = m_con + h*(P_B_m - L_B_m)

    return m1_con

# looping to find equilibrium state
# set n = 0
n=0
# set first iteration
# for Backward Euler
con_O_B_m = con_O0
con_NO2_B_m = con_NO20
con_NO_B_m = con_NO0
con_O3_B_m = con_O30
# for Foreward Euler
con_O_F_m = con_O0
con_NO2_F_m = con_NO20
con_NO_F_m = con_NO0
con_O3_F_m = con_O30

while n <= Np:
    # calculate production rate for Backward Euler
    P_O3_B_m = k1*con_O_B_m
    P_NO2_B_m = k2*con_NO_B_m*con_O3_B_m
    P_NO_B_m = J*con_NO2_B_m
    P_O_B_m = J*con_NO2_B_m

    # calculate loss rate/ m_con for Backward Euler
    V_O3_B_m = k2*con_NO_B_m
    V_NO2_B_m = J
    V_NO_B_m = k2*con_O3_B_m
    V_O_B_m = k1

    # calculate Backward Euler
    con_O3_B_m1 = Back_Euler(con_O3_B_m, P_O3_B_m, V_O3_B_m, h)
    con_NO2_B_m1 = Back_Euler(con_NO2_B_m, P_NO2_B_m, V_NO2_B_m, h)
    con_NO_B_m1 = Back_Euler(con_NO_B_m, P_NO_B_m, V_NO_B_m, h)
    con_O_B_m1 = Back_Euler(con_O_B_m, P_O_B_m, V_O_B_m, h)

    # calculate loss rate
    L_O3_B_m = V_O3_B_m*con_O3_B_m1
    L_NO2_B_m = V_NO2_B_m*con_NO2_B_m1
    L_NO_B_m = V_NO_B_m*con_NO_B_m1
    L_O_B_m = V_O_B_m*con_O_B_m1

    # calculate Forward Euler
    con_O3_F_m1 = Fore_Euler(con_O3_F_m, P_O3_B_m, L_O3_B_m, h)
    con_NO2_F_m1 = Fore_Euler(con_NO2_F_m, P_NO2_B_m, L_NO2_B_m, h)
    con_NO_F_m1 = Fore_Euler(con_NO_F_m, P_NO_B_m, L_NO_B_m, h)
    con_O_F_m1 = Fore_Euler(con_O_F_m, P_O_B_m, L_O_B_m, h)

    # store the value
    con_O3.append(con_O3_F_m1)
    con_NO2.append(con_NO2_F_m1)
    con_NO.append(con_NO_F_m1)
    con_O.append(con_O_F_m1)

    # test converging
    if (con_O3_F_m1 < 0) | (con_NO2_F_m1 < 0) | (con_NO_F_m1 < 0) | (con_O_F_m1 < 0):
        n = 0
    else:
        n = n+1

    # renew the initial concentration
    # for Backward Euler
    con_O_B_m = con_O_F_m1
    con_NO2_B_m = con_NO2_F_m1
    con_NO_B_m = con_NO_F_m1
    con_O3_B_m = con_O3_F_m1
    # for Foreward Euler
    con_O_F_m = con_O_F_m1
    con_NO2_F_m = con_NO2_F_m1
    con_NO_F_m = con_NO_F_m1
    con_O3_F_m = con_O3_F_m1


#################################################
### Plot the result
#################################################
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax2 = ax1.twinx()

# plot figure
plt_O = ax1.plot(h*np.arange(0, len(con_O)), np.array(con_O)*1e6, color = 'black', label = 'O(3P)*1e6')
plt_O3 = ax1.plot(h*np.arange(0, len(con_O3)), con_O3, color = 'green', label = 'O3')
plt_NO2 = ax1.plot(h*np.arange(0, len(con_NO2)), con_NO2, color = 'blue', label = 'NO2')
plt_NO = ax2.plot(h*np.arange(0, len(con_NO)), con_NO, color = 'red', label = 'NO')

ax1.set_xlabel('time (s)')
ax1.set_ylabel('Conc for O,O3,NO2 (molecules per cm^3)')
ax2.set_ylabel('Conc for NO (molecules per cm^3)')
ax1.set_title('Concentration of different chemical species')

ax1.text(330, 0.15e10, 'O(3P)*1e6', color = 'black', fontsize=12)
ax1.text(330, 0.35e10, 'O3', color = 'green', fontsize=12)
ax1.text(330, 0.5e10, 'NO2', color = 'blue', fontsize=12)
ax1.text(330, 0.93e10, 'NO', color = 'red', fontsize=12)
print(con_NO)
fig.savefig('L10_ex.png')