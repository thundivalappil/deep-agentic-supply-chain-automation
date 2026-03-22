import pandas as pd


def evaluate_demand(forecast_df: pd.DataFrame) -> dict:
    top_items = forecast_df.sort_values("forecast_qty", ascending=False).head(5)
    return {
        "top_demand_items": top_items[["sku", "location", "forecast_qty"]].to_dict(orient="records"),
        "message": "Demand agent identified the highest forecasted SKU-location combinations."
    }
