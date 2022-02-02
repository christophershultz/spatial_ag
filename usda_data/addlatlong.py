import pandas as pd
import numpy as np
import os, pdb

llmap = pd.read_csv("latlong_map.csv", encoding="ISO-8859-1")
llmap['fips'] = [str(i) for i in llmap['FIPS']]
llmap['fips'] = ['0'*(5-len(i)) + i if len(i) < 5 else i for i in llmap['fips']]
df = pd.read_csv(os.getcwd() + "\\usda_data\\joined_usda_df.csv", encoding="ISO-8859-1")
df['fips'] = [i.replace('-', '') for i in df['fips']]

llmap = llmap[['fips', 'Latitude', 'Longitude']]
df = pd.merge(df, llmap, how = 'left', on = 'fips')
df['netinc'] = [float(i.replace(',', '')) if str(i) != ' (D)' else 0.0 for i in df['netinc']]
df.to_csv(os.getcwd() + "\\usda_data\\" + "usda_with_lat_long.csv", index = None)