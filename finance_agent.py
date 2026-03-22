import pandas as pd


def evaluate_finance(plan_df: pd.DataFrame) -> dict:
    total_reorder_value = float(plan_df["reorder_value"].sum())
    high_value = plan_df.sort_values("reorder_value", ascending=False).head(5)
    return {
        "total_reorder_value": round(total_reorder_value, 2),
        "top_cash_impact_items": high_value[["sku", "location", "reorder_value"]].to_dict(orient="records"),
        "message": "Finance agent quantified working capital impact from replenishment actions."
    }
