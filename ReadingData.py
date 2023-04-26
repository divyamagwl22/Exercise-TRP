import pandas as pd 
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


