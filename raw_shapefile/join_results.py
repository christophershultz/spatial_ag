import geopandas as gpd
import os, pdb
import pandas as pd
import numpy as np

#Import shapefile and define fips. 
sf = gpd.read_file(os.getcwd() + "\\raw_shapefile\\cb_2018_us_county_5m.shp")
sf['fips'] = sf['STATEFP'] + sf['COUNTYFP']

#Import usda data and define fips. 
df = pd.read_csv(os.getcwd() + "\\usda_data\\usda_with_lat_long_imputed.csv", encoding="ISO-8859-1")
df['fips'] = [str(i) for i in df['fips']]
df['fips'] = ['0'*(5-len(i)) + i for i in df['fips']]
keeps = ['fips', 'netinc', 'fertilizer', 'fuel', 'labor', 'land', 'machinery', 'tractors', 'trucks']
df = df[keeps]

# Join residuals
resid = pd.read_csv(os.getcwd() + "\\results\\residuals.csv")
df['predicted'] = resid['yhat']
df['solow'] = df['netinc'] - df['predicted']
df['solow'] = [np.abs(i) for i in df['solow']]

# MERGE
sf = pd.merge(sf, df, how = 'left', on = 'fips')
sf['netinc'] = [float(i) for i in sf['netinc']]
sf['predicted'] = [float(i) for i in sf['predicted']]
sf['solow'] = [float(i) for i in sf['solow']]

# EXPORT
outfp = os.getcwd() + "\\results\\final_results.shp"
sf.to_file(outfp)