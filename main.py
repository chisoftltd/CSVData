# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     tempareture = []
# #     for row in data:
# #         if row[1] != "temp":
# #             tempareture.append(row[1])
# #     print(tempareture)
#
import pandas as pd

#
# data = pd.read_csv("weather_data.csv")
# print(type(data))
# print(type(data['temp']))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# print(sum(temp_list)/len(temp_list))
#
# print(data['temp'].mean())
#
# print(data['temp'].max())
# print(data.temp.max())
#
# #   Get Data in a row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# print(monday.temp)
# monday_temp = (monday.temp * (9/5)) + 32
# print(monday_temp)

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data['Primary Fur Color'])
print(data['Primary Fur Color'].count())
print(data['Primary Fur Color'].unique())

gray = data[data['Primary Fur Color'] == "Gray"]
cinnamon = data[data['Primary Fur Color'] == "Cinnamon"]
black = data[data['Primary Fur Color'] == "Black"]
nan = data[data['Primary Fur Color'] == "nan"]

print(gray['Primary Fur Color'])
print(gray['Primary Fur Color'].count())

print(cinnamon['Primary Fur Color'])
print(cinnamon['Primary Fur Color'].count())

print(black['Primary Fur Color'])
print(black['Primary Fur Color'].count())

print(nan['Primary Fur Color'])
print(nan['Primary Fur Color'].count())

s_colors = []
for color in data['Primary Fur Color'].unique():
    if color == 'Black':
        s_colors.append(black['Primary Fur Color'].count())
    elif color == "Cinnamon":
        s_colors.append(cinnamon['Primary Fur Color'].count())
    elif color == "Gray":
        s_colors.append(gray['Primary Fur Color'].count())

print(s_colors)
print(data['Primary Fur Color'].unique().tolist())

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray['Primary Fur Color'].count(), cinnamon['Primary Fur Color'].count(),
              black['Primary Fur Color'].count()]
}
print(data_dict)

data_csv = pd.DataFrame(data_dict)
print(data_csv.to_csv("squirrel_count.csv"))