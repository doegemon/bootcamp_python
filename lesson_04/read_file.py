# Reading a .csv file without using Pandas (using native Python library/package csv)
import csv

path: str = "data/data.csv"
data: list = []

# This function is kind of a Python API, and I'm creating a Dictionary from the .csv file with DictReader
with open(file=path, mode="r", encoding="utf-8") as file: 
  csv_reader: csv.DictReader = csv.DictReader(file)

  for row in csv_reader:
    data.append(row)

for r in data: 
  print(r)