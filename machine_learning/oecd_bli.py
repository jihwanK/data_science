import sklearn
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd

oecd_df = pd.read_csv('oecd_bli.csv', thousands=',')
# gdp_df = pd.read_csv('gdp_per_capita.tsv', sep='\t', thousands=',', encoding='latin1', na_values='n/a')
gdp_df = pd.read_csv('gdp.tsv', sep='\t', thousands=',', encoding='latin1', na_values='n/a')

print(oecd_df)
print(oecd_df.describe())
print(gdp_df)
print(gdp_df.describe())

# country_stats = prepare_country_stats()
