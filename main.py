import pandas as pd

data = pd.read_csv("weather_data.csv")
print(data)
print(data.head())
print(data.dtypes)