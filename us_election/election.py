import numpy as np
import pandas as pd

elections = pd.read_csv('./election/president_county_candidate.csv')
print(elections.county.value_counts())