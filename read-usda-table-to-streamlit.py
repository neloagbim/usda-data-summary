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

# use following for loading github csv when running locally
# download = requests.get(url).content
# Reading the downloaded content and turning it into a pandas dataframe
# df = pd.read_csv(io.StringIO(download.decode('utf-8')))

# read the url of the github csv
df = pd.read_csv(url)

# Printing out the first 5 rows of the dataframe to test results
#print (df.head())

base="dark"
# create streamlit header
st.header("USDA Datasets for Research Projects")

# add text input for searching description column
st.text_input("Search dataset description."," ")

# show dataframae as table
st.dataframe(df)
