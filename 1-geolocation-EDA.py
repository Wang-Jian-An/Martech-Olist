import numpy as np
import pandas as pd
from Variable import *

# %% Load Data
rawData = pd.read_csv(geolocationPath)
print(rawData.info())
print(rawData.head())

# %% Count each label
objFeatures = [geolocationPK, *[i for i in rawData.columns if rawData[i].dtype == "object" and not(i == geolocationPK)]]
for oneColumn in objFeatures:
    print("Feature: ", oneColumn)
    print("Total class: ", rawData[oneColumn].unique().__len__())
    print(rawData[oneColumn].value_counts())
    print("=" * 100)

# %% Explore someone geolocation_zip_code_prefix
print(rawData.query("geolocation_zip_code_prefix == 24220").head(), end = "\n" + "=" * 100 + "\n") 

# %% Confirm that each geolocation_zip_code_prefix have only geolocation_city and geolocation_state
uniqueGeolocationZipCodePrefix = rawData["geolocation_zip_code_prefix"].unique().tolist()
for oneZipCodePrefix in uniqueGeolocationZipCodePrefix:
    selectRawData = rawData.query("geolocation_zip_code_prefix == @oneZipCodePrefix")
    if selectRawData["geolocation_city"].unique().shape[0] != 1:
        print(oneZipCodePrefix, selectRawData["geolocation_city"].unique())
    print("=" * 100)
    if selectRawData["geolocation_state"].unique().shape[0] != 1:
        print(oneZipCodePrefix, selectRawData["geolocation_state"].unique())
    break