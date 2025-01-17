import pandas as pd

def load_csv_and_filter(csv_path: str, state: str) -> pd.DataFrame: 
    """
    Function that reads a .csv file and returns a DataFrame only with records from a
    state informed by the user when using the function.
    """
    df: pd.DataFrame = pd.read_csv(csv_path)
    
    df_non_na: pd.DataFrame = df.dropna()

    df_filtered: pd.DataFrame = df_non_na[df_non_na['state'] == state]

    return df_filtered


path_to_csv: str = 'example.csv'
state_to_filter: str = 'SP'
df_final: pd.DataFrame = load_csv_and_filter(csv_path=path_to_csv, state=state_to_filter)

print(df_final)
