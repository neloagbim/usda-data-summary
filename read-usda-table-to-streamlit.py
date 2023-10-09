# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 13:45:11 2023

@author: Nelo_Agbim
"""

import pandas as pd
import requests
import io
import streamlit as st

# Downloading the csv file from your GitHub account

url = "https://raw.githubusercontent.com/neloagbim/usda-data-summary/main/usda-datasets.csv" # Make sure the url is the raw version of the file on GitHub

#download = requests.get(url).content

# Reading the downloaded content and turning it into a pandas dataframe

#df = pd.read_csv(io.StringIO(download.decode('utf-8')))
df = pd.read_csv(url)

# Printing out the first 5 rows of the dataframe

print (df.head())

# create streamlit header

st.header("USDA Datasets for Research Projects")

st.dataframe(df)
