import pandas as pd

raw_data = pd.read_csv('German_cities_raw_data.csv', encoding='utf-16le')
print(raw_data.head())