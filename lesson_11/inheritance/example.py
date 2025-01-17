import pandas as pd

# Creating an abstract/parent class that will be used to create specific/children Classes
class ETLProcess:
    def __init__(self, data_source):
        self.data_source = data_source

    def extract_data(self):
        raise NotImplementedError("extract_data method must be implemented in the children classes.")
    
    def transform_data(self): 
        raise NotImplementedError("transform_data method must be implemented in the children classes.")
    
    def load_data(self):
        raise NotImplementedError("load_data method must be implemented in the children classes.")
    
    def start_etl(self):
        data_extracted = self.extract_data()
        data_transformed = self.transform_data(data_extracted)
        self.load_data(data_transformed)


# Creating a specific/child Class
class ETLCSV(ETLProcess):
    def extract_data(self):
        return pd.read_csv(self.data_source)
    
    def transform_data(self, data):
        return data.applymap(lambda x: x.upper() if isinstance(x, str) else x)
    
    def load_data(self, data_transformed):
        print(data_transformed)



# Use case
if __name__ == "__main__":
    csv_path: str = 'data.csv'
    # Creating a object from the Class created above
    etl_csv: ETLCSV = ETLCSV(csv_path)
    # Using the method of the Class/object to execute the ETL pipeline
    etl_csv.start_etl()
