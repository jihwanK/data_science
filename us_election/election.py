import numpy as np
import pandas as pd
import os

us_election_path = os.path.join(os.getcwd(), 'us_election')
file_path = os.path.join(us_election_path, 'election', 'president_county_candidate.csv')
elections = pd.read_csv(file_path)

print(elections.county.value_counts())