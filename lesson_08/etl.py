import os
import glob
import pandas as pd


def extract_and_concat_data(files_path: str) -> pd.DataFrame:
    """
    Function that receives a path with multiple .json files, reads and concats them into a
    single pandas Dataframe, returning this dataframe
    """
    json_files = glob.glob(os.path.join(files_path, "*.json"))
    df_list = [pd.read_json(file) for file in json_files]
    df_final = pd.concat(df_list, ignore_index=True)

    return df_final


def create_gmv_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function that receives a pandas Dataframe with sales data, and for each row calculates
    the GMV of the sale (Quantity * Price)
    """
    df_aux = df.copy()
    df_aux["GMV"] = df["Quantity"] * df["Price"]

    return df_aux


def export_data(df_final: pd.DataFrame, file_format: list) -> None:
    """
    Function that receives a pandas Dataframe and a list with the file format needed
    (csv, parquet or both). Based on the file format informed, it will export the
    dataframe to the file format informed.
    """
    for format in file_format:
        if format == "csv":
            df_final.to_csv("outputs/sales.csv", index=False)
        elif format == "parquet":
            df_final.to_parquet("outputs/sales.parquet", index=False)

    return None


def extract_transform_export_sales(
    json_file_paths: str, output_file_format: list
) -> None:
    """
    Function that consolidates all the functions above: reads and converts the .json files to
    a single pandas dataframe, creates the additional GMV column and exports to the file format
    informed by the final user.
    """
    df_initial: pd.DataFrame = extract_and_concat_data(json_file_paths)
    df_final: pd.DataFrame = create_gmv_column(df_initial)
    export_data(df_final, output_file_format)

    return None
