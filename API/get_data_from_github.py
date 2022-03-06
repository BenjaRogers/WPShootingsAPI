import pandas as pd

url = r'https://raw.githubusercontent.com/washingtonpost/data-police-shootings/master/fatal-police-shootings-data.csv'
data = pd.read_csv(url)
data.to_json(r'shooting_data.json', orient='records', indent=2, index=True)

