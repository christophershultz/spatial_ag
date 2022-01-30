import pandas as pd
import numpy as np
import os, pdb, sys

def netIncome(): 
    df = pd.read_csv('usda_data/net_income.csv')
    df = df[df['Year'] == 2017].reset_index().drop(['index'], axis = 1)
    df = df[['Year', 'State', 'State ANSI', 'County', 'County ANSI', 'Zip Code', 'Value']]
    df.columns = ['yr', 'st', 'st_ansi', 'cty', 'cty_ansi', 'zip', 'netinc']
    df['st_cty_yr'] = [df['st'][i] + '_' + df['cty'][i] + '_' + str(df['yr'][i]) for i in range(len(df))]
    print(str(len(df)))
    return df

def joinData(df, col):
    new = pd.read_csv('usda_data/' + col + '.csv')
    if col == 'labor': new = new[new['Domain'] == 'TOTAL'].reset_index().drop(['index'], axis = 1)
    new = new[['Year', 'State', 'State ANSI', 'County', 'County ANSI', 'Zip Code', 'Value']]
    new.columns = ['yr', 'st', 'st_ansi', 'cty', 'cty_ansi', 'zip', col]
    new['st_cty_yr'] = [new['st'][i] + '_' + new['cty'][i] + '_' + str(new['yr'][i]) for i in range(len(new))]
    new = new[['st_cty_yr', col]]
    df = pd.merge(df, new, how = 'left', on = 'st_cty_yr')
    print(str(len(df)))
    return df

def updateFips(df): 
    df['st_ansi'] = [str(i) for i in df['st_ansi']]
    df['st_ansi'] = ['0' + i if len(i) == 1 else i for i in df['st_ansi']]
    df['cty_ansi'] = [int(i) if str(i).lower() != 'nan' else 0 for i in df['cty_ansi']]
    df['cty_ansi'] = [str(i) for i in df['cty_ansi']]
    df['cty_ansi'] = ['0'*(3-len(i)) + i if len(i) != 3 else i for i in df['cty_ansi']]
    df['fips'] = [st + '-' + cty for st, cty in zip(df['st_ansi'], df['cty_ansi'])]
    return df

def main(): 
    df = netIncome()
    for column in ['fertilizer', 'fuel', 'labor', 'land', 'machinery', 'tractors', 'trucks']: 
        print("Joining " + column)
        df = joinData(df, column)
    df = updateFips(df)
    df.to_csv('usda_data/joined_usda_df.csv', index = None)

main()