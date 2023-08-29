import pandas as pd

# Data loading
raw_data = pd.read_csv('German_cities_raw_data.csv', encoding='utf-16le', sep='\t')

# Filter: Relevant columns
relevant_cols = ['city', 'federal state', 'population 2015', 'delta [%] (2014-2015)']

# Order by: Population (desc)
per_population_data = raw_data.sort_values(by='population 2015', ascending=False)
print(per_population_data[relevant_cols][:15])

# Group by Land. Determine the most populated Länder
data_grouped = raw_data.groupby("federal state")

all_results = {"federal state": [], "population 2015": []}

for name, group in data_grouped:
    all_results["federal state"].append(name)
    all_results["population 2015"].append(group["population 2015"].sum())

table_federal_state = pd.DataFrame(all_results).sort_values(by="population 2015", ascending=False)
print(table_federal_state.head())