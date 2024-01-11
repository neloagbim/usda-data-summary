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


# create streamlit header
st.title("USDA Datasets for Research Projects")
# create streamlit title
st.text("Here is a list of USDA datasets for undergraduate students studying food and agriculture")

# add text input for searching description column
search_word = st.text_input("Search dataset description."," ")

df_search = df[df["description"].str.contains(search_word)==True]

if len(search_word) == 0:  
  # show dataframae as table
  st.dataframe(df)
else:
  st.dataframe(df_search)
