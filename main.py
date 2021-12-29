import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    tempareture = []
    for row in data:
        if row[1] != "temp":
            tempareture.append(row[1])
    print(tempareture)