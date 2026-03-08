from pathlib import Path
import pandas

# data = pandas.read_csv(Path(__file__).with_name("weather_data.csv"))
# print(data[data['temp'] == data['temp'].max()])

data = pandas.read_csv(Path(__file__).with_name("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"))
counts = data["Primary Fur Color"].value_counts()
counts.to_csv(Path(__file__).with_name("fur_color_counts.csv"))