import pandas as pd


def evaluate_logistics(plan_df: pd.DataFrame) -> dict:
    urgent_shipments = plan_df[plan_df["urgency"] == "High"]
    return {
        "urgent_shipments": urgent_shipments[["sku", "location", "urgency"]].head(5).to_dict(orient="records"),
        "message": "Logistics agent recommends expedited treatment for high-urgency items."
    }
