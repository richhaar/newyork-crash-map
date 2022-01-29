# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 18:10:31 2022

Visualising Crash data from New York City, available from NYC open data here:
https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95

@author: Richard Haar
"""

# %% Import the Dataset, assumed in subfolder
# datasets/ny/Motor_Vehicle_Collisions_-_Crashes.csv

import os
import pandas as pd

DATA_PATH = os.path.join("datasets", "ny")
DATA_NAME = "Motor_Vehicle_Collisions_-_Crashes.csv"

def load_data(data_path=DATA_PATH, data_name=DATA_NAME):
    csv_path = os.path.join(data_path, DATA_NAME)
    return pd.read_csv(csv_path)

crashdata = load_data()

# %% Data exploration

print(crashdata.head())
print(crashdata.info())

# Misc injury statistics

print(crashdata.iloc[:, 10:18].sum())
# NUMBER OF PERSONS INJURED        528270.0
# NUMBER OF PERSONS KILLED           2492.0
# NUMBER OF PEDESTRIANS INJURED     97629.0
# NUMBER OF PEDESTRIANS KILLED       1283.0
# NUMBER OF CYCLIST INJURED         44811.0
# NUMBER OF CYCLIST KILLED            186.0
# NUMBER OF MOTORIST INJURED       383340.0
# NUMBER OF MOTORIST KILLED          1008.0

print(crashdata.iloc[:, 10:18].max())
# NUMBER OF PERSONS INJURED        43.0
# NUMBER OF PERSONS KILLED          8.0
# NUMBER OF PEDESTRIANS INJURED    27.0
# NUMBER OF PEDESTRIANS KILLED      6.0
# NUMBER OF CYCLIST INJURED         4.0
# NUMBER OF CYCLIST KILLED          2.0
# NUMBER OF MOTORIST INJURED       43.0
# NUMBER OF MOTORIST KILLED         5.0

subcrash = crashdata
subcrash.dropna(subset=["LONGITUDE","LATITUDE"])

med = crashdata[["LONGITUDE", "LATITUDE"]].median()
offset = 0.1

subcrash.plot(kind="scatter", x="LONGITUDE", y="LATITUDE", alpha=0.01, s=0.02,
              xlim=[med[0]-offset,med[0]+offset],
              ylim=[med[1]-offset,med[1]+offset])

"""
Alternate way of subsampling data

subcrash = subcrash[subcrash.LONGITUDE > -74.4]
subcrash = subcrash[subcrash.LONGITUDE < -70]
subcrash = subcrash[subcrash.LATITUDE < 41]

subcrash.plot(kind="scatter", x="LONGITUDE", y="LATITUDE", alpha= 0.01, s=0.1)
"""