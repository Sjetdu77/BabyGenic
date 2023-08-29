import pandas as pd

# Data loading
raw_data = pd.read_csv('German_cities_raw_data.csv', encoding='utf-16le', sep='\t')
print(raw_data.head())

# Filter: Relevant columns
relevant_cols = ['city', 'federal state', 'population 2015', 'delta [%] (2014-2015)']

# Order by: Population (desc)
per_population_data = raw_data.sort_values(by='population 2015', ascending=False)
print(per_population_data[relevant_cols][:15])