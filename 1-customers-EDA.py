import numpy as np
import pandas as pd
from Variable import *

# %% Load Data
rawData = pd.read_csv(customersPath)
print(rawData.info())
print(rawData.head()) 

# %% Count each label
objFeatures = [i for i in rawData.columns if rawData[i].dtype == "object"]
for oneColumn in objFeatures:
    print("Feature: ", oneColumn)
    print("Total class: ", rawData[oneColumn].unique().__len__())
    print(rawData[oneColumn].value_counts())
    print("=" * 100)