import pandas as pd


class CsvProcessor:
    # Creating the constructor method
    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.df = None
        self.df_filtered = None

    # Creating the method to read the .csv file
    def load_csv(self):
        self.df = pd.read_csv(self.csv_path)
        return self.df

    # Creating the method to filter the Dataframe
    def filter_by(self, columns, values):
        if len(columns) != len(values):
            raise ValueError("The number of columns and values is not the same.")

        if len(columns) == 0:
            return self.df

        current_column = columns[0]
        current_value = values[0]

        df_filtered = self.df[self.df[current_column] == current_value]

        if len(columns) == 1:
            return df_filtered
        else:
            # Recursive method
            return self.filter_by(columns[1:], values[1:])
