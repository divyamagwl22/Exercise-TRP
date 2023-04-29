import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

Pressure1 = pd.read_csv('Public Projects\Exercise-TRP\Pressure1.csv')
P1 = Pressure1.to_numpy() #PS0 / Ticks [us]

for i in np.arange(0,len(P1[:,1])):
    P1[i,0] = P1[i,0] * 6250 - 24
    P1[i,1] = P1[i,1]/10E+6 

P1[:,1] = P1[:,1] - P1[70000,1]

plt.plot(P1[70000:90000,1],P1[70000:90000,0])
plt.show()