# usda-data-summary
Purpose: Interactive table showing all available datasets for USDA.

This project takes a JSON of datasets from USDA's website, transforms it into a table, and reads that table into streamlit where it can be filtered by description. The idea behind this project came about from my graduate school days when undergraduates I worked with needed help finding datasets to do their Senior thesis or participate in a research group. When I was a student I would have loved having something like this available.

There are 2 scripts in this repository.

1) Reads the USDA json directly from their website, transforms it into a dataframe that describes the dataset, and saves it to a google sheet.
2) Creates a streamlit app where the dataframe can be filtered by description of the dataset.



