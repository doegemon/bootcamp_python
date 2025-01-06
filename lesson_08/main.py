from etl import extract_transform_export_sales

files_path = "data"
output_format = ["csv", "parquet"]

extract_transform_export_sales(
    json_file_paths=files_path, output_file_format=output_format
)
