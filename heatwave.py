import pandas as pd

# File names and extension
csv_extension = ".csv"
dados2 = "dados_2"
tmin_iac = "tmin_iac"

# Opens CSV and reads into dataframe
max_temps = pd.read_csv(dados2+csv_extension, sep=';')
min_temps = pd.read_csv(tmin_iac+csv_extension)

# Gets the max temperature for both locations 
max_cepagri = max_temps.loc[:,'IAC']
max_cepagri = max_temps['Cepagri']
# Gets the min temperature for both locations
min_iac = min_temps['IAC']
min_cepagri = min_temps['Cepagri']

