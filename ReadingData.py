import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from scipy.interpolate import splev, splrep, UnivariateSpline

# DATA 1
# Read CSV file for Thermocouple data from Datasheet 1
Thermocouples1 = pd.read_csv('Thermocouples1.csv')
# Convert data to numpy accessable
T1 = Thermocouples1.to_numpy()
Pressure1 = pd.read_csv('Pressure1.csv')
P1 = Pressure1.to_numpy()
Load1 = pd.read_csv('Load1.csv')
L1 = Load1.to_numpy()

# DATA 2
Thermocouples2 = pd.read_csv('Thermocouples2.csv')
T2 = Thermocouples2.to_numpy()
Pressure2 = pd.read_csv('Pressure2.csv')
P2 = Pressure2.to_numpy()
Load2 = pd.read_csv('Load2.csv')
L2 = Load2.to_numpy()

# Example: Index out 3rd column from Thermocouple sheet
print(T2[:,3])

#calculation of regression rate 
a = 5.132 #mm/s/MPa
n = 0.222 # 

# Calibrate Pressure 1 data
for i in np.arange(0, len(P1[:, 1])):
    P1[i, 0] = P1[i, 0] * 6250 - 24
    P1[i, 0] = P1[i, 0]/10
    P1[i, 1] = P1[i, 1] / 1e7

# Calibrate Pressure 2 data
for i in np.arange(0, len(P2[:, 1])):
    P2[i, 0] = P2[i, 0] * 6250 - 24
    P2[i, 0] = P2[i, 0]/10
    P2[i, 1] = P2[i, 1] / 1e7

# Calculate regression rate for Pressure 1
P1_pressure = P1[:, 0]
P1_time = P1[:, 1]
regression_rate_P1 = a * (P1_pressure ** n)

# Calculate regression rate for Pressure 2
P2_pressure = P2[:, 0]
P2_time = P2[:, 1]
regression_rate_P2 = a * (P2_pressure ** n)

# Adjust time for Pressure 1
P1[:, 1] = P1[:, 1] - P1[70000, 1]\

#Adjust time for Pressure 2
P2[:, 1] = P2[:, 1] - P2[60000, 1]\

# Apply UnivariateSpline for Pressure 1 data from 70000 to 90000
spl_P1 = UnivariateSpline(P1[70000:90000, 1], P1[70000:90000, 0], s=3000)
x2_P1 = np.arange(P1[70000, 1], P1[90000, 1], 0.01)
y2_P1 = spl_P1(x2_P1)

# Apply UnivariateSpline for Pressure 2 data from 60000 to 120000
spl_P2 = UnivariateSpline(P2[60000:120000, 1], P2[60000:120000, 0], s=2900)
x2_P2 = np.arange(P2[60000, 1], P2[120000, 1], 0.01)
y2_P2 = spl_P2(x2_P2)

# Plot the Pressure 1 data with the spline curve
plt.figure(figsize=(10, 5))
plt.plot(P1[70000:90000, 1], P1[70000:90000, 0], "o", label='Data')
plt.plot(x2_P1, y2_P1, "r-", label='Spline curve')
plt.xlabel('Time (seconds)')
plt.ylabel('Regression Rate')
plt.title('Regression Rate vs Time')
plt.legend()
plt.grid(True)
plt.show()

# Plot the Pressure 2 data with the spline curve
plt.figure(figsize=(10, 5))
plt.plot(P2[60000:120000, 1], P2[60000:120000, 0], "o", label='Data')
plt.plot(x2_P2, y2_P2, "r-", label='Spline curve')
plt.xlabel('Time (seconds)')
plt.ylabel('Regression Rate')
plt.title('Regression Rate vs Time')
plt.legend()
plt.grid(True)
plt.show()