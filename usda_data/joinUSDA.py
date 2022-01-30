import pandas as pd
import numpy as np
import os, pdb, sys

def netIncome(): 
    df = pd.read_csv('net_income.csv')
    keeps = ['Year', 'State', 'State ANSI', 'County', 'County ANSI', 'Zip Code', 'Value']
    df = df[keeps]
    df.columns = ['yr', 'st', 'st_ansi', 'cty', 'cty_ansi', 'zip', 'netinc']
    df['st_cty_yr'] = [df['st'][i] + '_' + df['cty'][i] + '_' + str(df['yr'][i]) for i in range(len(df))]
    return df

def joinData(df, col):
    new = pd.read_csv(col + '.csv')
    keeps = ['Year', 'State', 'State ANSI', 'County', 'County ANSI', 'Zip Code', 'Value']
    new = new[keeps]
    new.columns = ['yr', 'st', 'st_ansi', 'cty', 'cty_ansi', 'zip', col]
    new['st_cty_yr'] = [new['st'][i] + '_' + new['cty'][i] + '_' + str(new['yr'][i]) for i in range(len(new))]
    new = new[['st_cty_yr', col]]
    df = pd.merge(df, new, how = 'left', on = 'st_cty_yr')
    return df

def main(): 
    df = netIncome()
    for column in ['fertilizer', 'fuel', 'labor', 'land', 'machinery', 'tractors', 'trucks']: 
        print("Joining " + column)
        df = joinData(df, column)
    pdb.set_trace()
    df.to_csv('joined_usda_df.csv', index = None)

main()