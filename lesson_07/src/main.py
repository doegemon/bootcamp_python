from etl import read_csv, sales_delivered, gmv_sales_delivered

file_path = "../data/sales.csv"

all_sales = read_csv(csv_path=file_path)
delivered_sales = sales_delivered(all_sales)
gmv_dlv_sales = gmv_sales_delivered(delivered_sales)

print(f"The total GMV of the delivered sales is {gmv_dlv_sales}.")
