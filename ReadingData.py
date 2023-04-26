import pandas as pd 
# DATA 1
Thermocouples1 = pd.read_excel('Data 1.xlsb', engine='pyxlsb', sheet_name= 'Thermocouples')
Pressure1 = pd.read_excel('Data 1.xlsb', engine='pyxlsb', sheet_name= 'Pressure Sensors')
Load1 = pd.read_excel('Data 1.xlsb', engine='pyxlsb', sheet_name= 'Load Cells')

# DATA 2
Thermocouples2 = pd.read_excel('Data 2.xlsx', sheet_name= 'Thermocouples')
Pressure2 = pd.read_excel('Data 2.xlsx', sheet_name= 'Pressure Sensors')
Load2 = pd.read_excel('Data 2.xlsx', sheet_name= 'Load Cells')

print(Load2)

