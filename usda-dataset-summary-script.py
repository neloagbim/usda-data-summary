# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 16:25:37 2023

@author: Nelo_Agbim
"""

import pandas as pd
import requests
#import json
#from bs4 import BeautifulSoup
from tqdm import tqdm

# request usda json with dataset information
result = requests.get('https://www.usda.gov/sites/default/files/documents/data.json' )
# save result as json
jresult = result.json()

#print json keys
jresult.keys()

# save dataset entry as a seperate variable
datasets = jresult['dataset']

# sample of keys in each dataset
info = list( datasets[0].keys())

# initiate dataframe to hold dataset information
df = pd.DataFrame(columns=["title", "description", "author", "contact","email_contact", "update_date","url","data_type","access"])

x = 0
for x in tqdm(range(len(datasets) - 1)): 
    # extract df info and save as variables
    title = datasets[x]['title']
    desc = datasets[x]['description']
    author = datasets[x]['publisher']['name']
    contact = datasets[x]['contactPoint']['fn']
    email_contact = datasets[x]['contactPoint']['hasEmail']
    update_date = datasets[x]['modified']
    try:
        # if there is distibution info grab it
        if len(datasets[x]['distribution'])>0:
             #if url is stored in download key, grab it from there
             if  "downloadURL" in  list(datasets[x]['distribution'][0].keys()): #type(datasets[x]['distribution'])  == list
                 url = datasets[x]['distribution'][0]['downloadURL']
                 data_type = datasets[x]['distribution'][0]['mediaType']
             # if there is no downlaodurl key, try the accessurl key
             elif "accessURL" in  list(datasets[x]['distribution'][0].keys()):
                 url = datasets[x]['distribution'][0]['accessURL']
                 data_type = datasets[x]['distribution'][0]['@type']
             # otherwise get te landing page url and leave data type blank
             else:
                url = datasets[x]['landingPage']
                data_type = None 
        # if there was no distribution info, grab the landing page
        else:
            url = datasets[x]['landingPage']
            data_type = None 
    except:
         url = None
         data_type = None
    # save access 
    access = datasets[x]['accessLevel']
    # save info to dataframe
    df.loc[len(df.index)] = [title, desc, author, contact, email_contact, update_date,url, data_type,access]

import gspread
from gspread_dataframe import set_with_dataframe
from google.oauth2.service_account import Credentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# scope of where api will work
scopes = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']

credentials = Credentials.from_service_account_file(r'C:\Users\NeloAgbim\Documents\Google Sheets Python Json\my-github-projects-410915-057cbdd1bc31.json',  scopes=scopes)
gc = gspread.authorize(credentials)

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

# open the google sheet
gs = gc.open_by_url('https://docs.google.com/spreadsheets/d/13QpkebvBdk0bWTkX0gtWhcRe8WVVlPbyA2LUyGFZ7TI/edit#gid=0')
# select a work sheet from its name
worksheet = gs.worksheet('cleaned')

# write to google sheet
# clear out any contents
worksheet.clear()
set_with_dataframe(worksheet, dataframe=df, include_index=False,include_column_header=True,resize=True)

df.to_csv(r"C:\Users\NeloAgbim\Documents\PythonPrjEnvs\usdasummary\github\usda-datasets.csv",index=False)