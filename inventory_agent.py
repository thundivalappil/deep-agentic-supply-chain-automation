import pandas as pd


def evaluate_inventory(plan_df: pd.DataFrame) -> dict:
    risky = plan_df[plan_df["urgency"] == "High"].sort_values("reorder_value", ascending=False)
    return {
        "high_urgency_count": int(len(risky)),
        "inventory_alerts": risky[["sku", "location", "on_hand", "reorder_qty", "urgency"]].head(5).to_dict(orient="records"),
        "message": "Inventory agent flagged low-cover items needing faster replenishment."
    }
