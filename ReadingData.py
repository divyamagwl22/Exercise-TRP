import pandas as pd 
# DATA 1
Thermocouples1 = pd.read_csv('Thermocouples1.csv')
Pressure1 = pd.read_csv('Pressure1.csv')
Load1 = pd.read_csv('Load1.csv')


# DATA 2
Thermocouples2 = pd.read_csv('Thermocouples2.csv')
Pressure2 = pd.read_csv('Pressure2.csv')
Load2 = pd.read_csv('Load2.csv')

print(Load2[:,0])


