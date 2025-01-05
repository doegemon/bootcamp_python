import csv


def read_csv(csv_path: str) -> list[dict]:
    """
    Function that reads a .csv file and returns a list of dictionaries
    """
    sales_list: list[dict] = []

    with open(csv_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            sales_list.append(row)

    return sales_list


def sales_delivered(sales: list[dict]) -> list[dict]:
    """
    Function that receives the sales list and returns the sales
    where the product has been delivered
    """
    filtered_list: list[dict] = []
    for sale in sales:
        if sale.get("delivered") == "True":
            filtered_list.append(sale)

    return filtered_list


def gmv_sales_delivered(dlv_sales: list[dict]) -> float:
    """
    Function that receives the sales delivered list and returns the sum
    of the GMV of the sales delivered.
    """
    total_gmv: float = 0
    for dlv_sale in dlv_sales:
        price: float = float(dlv_sale.get("price"))
        qnt: float = float(dlv_sale.get("quantity"))
        gmv: float = price * qnt
        total_gmv += gmv

    return total_gmv
