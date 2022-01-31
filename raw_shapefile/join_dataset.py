import geopandas as gpd
import os, pdb
import pandas as pd

#Import shapefile and define fips. 
sf = gpd.read_file(os.getcwd() + "\\raw_shapefile\\cb_2018_us_county_5m.shp")
sf['fips'] = sf['STATEFP'] + sf['COUNTYFP']

#Import usda data and define fips. 
df = pd.read_csv(os.getcwd() + "\\usda_data\\joined_usda_df.csv")
df['fips'] = [i.replace('-', '') for i in df['fips']]
df = df[df['netinc'] != ' (D)'].reset_index().drop(['index'], axis = 1)
keeps = ['fips', 'netinc', 'fertilizer', 'fuel', 'labor', 'land', 'machinery', 'tractors', 'trucks']
df = df[keeps]

# Remove commas
for col in keeps[1:]: 
    new = [] 
    for value in df[col]: 
        try: 
            new.append(float(value.replace(',', '')))
        except: 
            new.append(0)
    df[col] = new

# MERGE
sf = pd.merge(sf, df, how = 'left', on = 'fips')
sf['netinc'] = [float(i) for i in sf['netinc']]

# EXPORT
outfp = os.getcwd() + "\\joined_shapedata\\ag.shp"
sf.to_file(outfp)