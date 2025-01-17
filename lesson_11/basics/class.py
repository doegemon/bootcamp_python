import pandas as pd

# creating a Class to do the whole process
class CSVProcess:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None

    def load_csv(self):
        # Reads .csv file and creates a DataFrame
        self.df = pd.read_csv(self.csv_path)

    def null_filter(self):
        # Remove null records
        self.df = self.df.dropna()

    def state_filter(self, state):
        # Using a specific state to filter records
        self.df = self.df[self.df['state'] == state]

    def process(self, state):
        # Load .csv, remove null records and filter records
        self.load_csv()
        self.null_filter()
        self.state_filter(state)

        return self.df
    

path_to_csv: str = 'example.csv'
state_to_filter: str = 'SP'

# Creating a object from the Class created above
processor: CSVProcess = CSVProcess(path_to_csv)
# Using the methods of the Class/object to get the filtered DataFrame
df_final: pd.DataFrame = processor.process(state_to_filter)

print(df_final)
