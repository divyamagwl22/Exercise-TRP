import pandas as pd 
# DATA 1
Thermocouples1 = pd.read_excel('Data 1.xlsb', engine='pyxlsb', sheet_name= 'Thermocouples')
Thermocouples1.to_csv('Thermocouples1', index=False)
Pressure1 = pd.read_excel('Data 1.xlsb', engine='pyxlsb', sheet_name= 'Pressure Sensors')
Pressure1.to_csv('Pressure1', index=False)
Load1 = pd.read_excel('Data 1.xlsb', engine='pyxlsb', sheet_name= 'Load Cells')
Load1.to_csv('Load1', index=False)

# DATA 2
Thermocouples2 = pd.read_excel('Data 2.xlsx', sheet_name= 'Thermocouples')
Thermocouples2.to_csv('Thermocouples2', index=False)
Pressure2 = pd.read_excel('Data 2.xlsx', sheet_name= 'Pressure Sensors')
Pressure2.to_csv('Pressure2', index=False)
Load2 = pd.read_excel('Data 2.xlsx', sheet_name= 'Load Cells')
Load2.to_csv('Load2', index=False)


