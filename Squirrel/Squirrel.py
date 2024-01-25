# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
#     print(temperature)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(sum(data["temp"]) / len(data["temp"]))
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.condition) # same as data["condition"] # get column

# get row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# create dataFrame
# data_dict = {
#     "students": ["sahil", "zeel"],
#     "scores": [96, 69]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("marks.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240111.csv")

gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray, black, cinnamon]
}
df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")
