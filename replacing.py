import numpy as np
import pandas as pd


df = pd.read_csv("adult.data.asha.csv")

#df[' Native Country'] = df[' Native Country'].replace(' ?', np.nan)
#df[' Workclass'] = df[' Workclass'].replace(' ?', np.nan)
#df[' Occupation'] = df[' Occupation'].replace(' ?', np.nan)
#df.dropna(inplace=True)

#df.drop([' Final Weight', ' Capital Gain', ' Capital Loss'], axis=1, inplace=True)

df[' Occupation'] = df[' Occupation'].replace({' Adm-clerical':1, ' Armed-forces': 2, ' Craft-repair':3, ' Exec-managerial':4, ' Farming-fishing':5, ' Handlers-cleaners':6, ' Machine-op-inspct':7, ' Other-service':8, ' Priv-house-serv':9, ' Prof-specialty':10, ' Protective-serv':11, ' Sales':12, ' Tech-support':13, ' Transport-moving':14})
df[' Relationship'] = df[' Relationship'].replace({' Husband':1,' Not-in-family':2, ' Other-relative':3, ' Own-child':4, ' Unmarried':5, ' Wife':6})
#df.drop([' Native Country'], axis=1, inplace=True)
df.dropna(inplace=True)

df.to_csv("adult.data.asha.csv", index = False)
