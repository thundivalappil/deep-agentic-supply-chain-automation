import pandas as pd


def load_sales_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def load_inventory_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def load_suppliers_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)
