import pandas as pd


REQUIRED_SALES_COLS = {"date", "sku", "location", "qty"}
REQUIRED_INV_COLS = {"sku", "location", "on_hand", "lead_time_days", "unit_cost"}
REQUIRED_SUPPLIER_COLS = {"sku", "preferred_supplier", "supplier_risk", "moq"}


def validate_inputs(
    sales: pd.DataFrame,
    inventory: pd.DataFrame,
    suppliers: pd.DataFrame,
) -> None:
    missing_sales = REQUIRED_SALES_COLS - set(sales.columns)
    missing_inv = REQUIRED_INV_COLS - set(inventory.columns)
    missing_sup = REQUIRED_SUPPLIER_COLS - set(suppliers.columns)

    if missing_sales:
        raise ValueError(f"Missing sales columns: {sorted(missing_sales)}")
    if missing_inv:
        raise ValueError(f"Missing inventory columns: {sorted(missing_inv)}")
    if missing_sup:
        raise ValueError(f"Missing supplier columns: {sorted(missing_sup)}")
