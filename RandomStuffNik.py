import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splev, splrep, UnivariateSpline

Pressure1 = pd.read_csv('Public Projects\Exercise-TRP\Pressure1.csv')
P1 = Pressure1.to_numpy() #PS0 / Ticks [us]
Load1 = pd.read_csv('Public Projects\Exercise-TRP\Load1.csv')
L1 = Load1.to_numpy()
Load2 = pd.read_csv('Public Projects\Exercise-TRP\Load2.csv')
L2 = Load2.to_numpy()
#Pressure Plot
for i in np.arange(0,len(P1[:,1])):
    P1[i,0] = P1[i,0] * 6250 - 24
    P1[i,1] = P1[i,1]/10E+6 

P1[:,1] = P1[:,1] - P1[70000,1]
#spl_P1 = splrep(P1[70000:90000,1], P1[70000:90000,0])
#x2_P1 = np.arange(P1[70000,1],P1[90000,1], 0.01)
#y2_P1 = splev(x2_P1, spl_P1)

#plt.plot(P1[70000:90000,1],P1[70000:90000,0],"o",x2_P1,y2_P1)
#plt.show()
#Load cell Plot
for i in np.arange(0,len(L1[:,1])):
    L1[i,0] = L1[i,0] * (-1087254) - 63.2972
    L1[i,1] = L1[i,1]/10E+6 

for i in np.arange(0,len(L2[:,1])):
    L2[i,0] = L2[i,0] * (-1087254) - 63.2972
    L2[i,1] = L2[i,1]/10E+6 

#spl_L1 = splrep(L1[70000:90000,1], L1[70000:90000,0])
#x2_L1 = np.arange(L1[70000,1],L1[90000,1], 0.01)
#y2_L1 = splev(x2_L1, spl_L1)

spl_L2 = UnivariateSpline(L2[80000:120000,1], L2[80000:120000,0],s=len(L2[80000:120000,0]),k=5)
x2_L2 = np.arange(L2[80000,1],L2[120000,1],0.01)

plt.plot(L2[80000:120000,1],L2[80000:120000,0],c="r")
plt.plot(x2_L2,spl_L2(x2_L2),c='b')
plt.show()

