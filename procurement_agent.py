import pandas as pd


def evaluate_procurement(plan_df: pd.DataFrame) -> dict:
    purchase_needed = plan_df[plan_df["reorder_qty"] > 0].copy()
    total_value = float(purchase_needed["reorder_value"].sum())
    return {
        "total_purchase_value": round(total_value, 2),
        "priority_orders": purchase_needed[["sku", "preferred_supplier", "reorder_qty", "reorder_value"]].head(5).to_dict(orient="records"),
        "message": "Procurement agent summarized supplier-linked reorder priorities."
    }
