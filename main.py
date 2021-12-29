# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     tempareture = []
#     for row in data:
#         if row[1] != "temp":
#             tempareture.append(row[1])
#     print(tempareture)

import pandas as pd

data = pd.read_csv("weather_data.csv")
print(type(data))
print(type(data['temp']))

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(temp_list)

print(sum(temp_list)/len(temp_list))

print(data['temp'].mean())

print(data['temp'].max())
print(data.temp.max())

#   Get Data in a row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

print(monday.temp)
monday_temp = (monday.temp * (9/5)) + 32
print(monday_temp)