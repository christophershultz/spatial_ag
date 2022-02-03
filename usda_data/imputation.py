import pandas as pd
import numpy as np
import os, pdb

root = os.getcwd() + "\\usda_data\\"

df = pd.read_csv(root + 'usda_with_lat_long.csv',encoding="ISO-8859-1")
df['fertilizer'] = [float(i.replace(',', '')) if str(i).lower() != 'nan' else 99999999 for i in df['fertilizer']]
df['fuel'] = [float(i.replace(',', '')) if str(i).lower() != 'nan' else 99999999 for i in df['fuel']]
df['labor'] = [float(i.replace(',', '')) if str(i).lower() != 'nan' else 99999999 for i in df['labor']]
df['land'] = [float(i.replace(',', '')) if str(i).lower() != 'nan' else 99999999 for i in df['land']]
df['machinery'] = [float(i.replace(',', '')) if str(i).lower() != 'nan' else 99999999 for i in df['machinery']]
df['tractors'] = [float(i.replace(',', '')) if str(i).lower() != 'nan' else 99999999 for i in df['tractors']]
df['trucks'] = [float(i.replace(',', '')) if str(i).lower() != 'nan' else 99999999 for i in df['trucks']]

def fixCols(col, df): 
    print("Fixing " + col)
    vals = []
    for i in range(len(df)): 
        currVal = df[col][i]
        if currVal == 99999999: 
            st = df['st'][i]
            sub = df[df['st'] == st]
            avg = np.mean([i for i in sub[col] if i != 99999999])
            vals.append(avg)
        else: 
            vals.append(currVal)
    return vals

for col in ['netinc', 'fertilizer', 'fuel', 'labor', 'land', 'machinery', 'tractors', 'trucks']: 
    df[col] = fixCols(col, df)

df.to_csv('usda_with_lat_long_imputed.csv', index = None)