# usda-data-summary
Purpose: Live spreadsheet showing all available datasets for USDA.

This project takes a JSON of datasets from USDA's website, transforms it into a table, and reads that table into googlesheets where it can be viewed. The idea behind this project came about from my graduate school days when undergraduates I worked with needed help finding datasets to do their Senior thesis or participate in a research group. If there was a spreadsheet with datasets, it was rarely an automated list. When I was a student I would have loved having something like this available.

The primary script in this repository does the following:

1) Reads the USDA json directly from their website.
2) Transforms it into a dataframe that describes the dataset.
3) Finally, it  saves the dataframe to a google sheet.

1) Script: usda-dataset-summary-script.py
2) Input: https://www.usda.gov/content/usda-open-data-catalog
3) Output: https://docs.google.com/spreadsheets/d/13QpkebvBdk0bWTkX0gtWhcRe8WVVlPbyA2LUyGFZ7TI/edit#gid=0




