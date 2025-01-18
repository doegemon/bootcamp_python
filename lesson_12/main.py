from csv_class import CsvProcessor

file_path: str = "example.csv"
filters: list = ["state", "price"]
values: list = ["SP", 10.50]

csv_file = CsvProcessor(file_path)
csv_file.load_csv()

print(csv_file.df)
print("--=--=--=--=--=--=--=--=--")
print(csv_file.filter_by(filters, values))
