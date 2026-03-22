import pandas as pd


def evaluate_risk(plan_df: pd.DataFrame) -> dict:
    high_risk = plan_df[plan_df["supplier_risk"].str.lower() == "high"]
    return {
        "high_supplier_risk_count": int(len(high_risk)),
        "risk_items": high_risk[["sku", "preferred_supplier", "supplier_risk", "urgency"]].head(5).to_dict(orient="records"),
        "message": "Risk agent highlighted supplier concentration and disruption exposure."
    }
