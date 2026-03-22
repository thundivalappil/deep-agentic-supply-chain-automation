import pandas as pd


def optimize_reorder(
    forecast_df: pd.DataFrame,
    inventory_df: pd.DataFrame,
    suppliers_df: pd.DataFrame,
) -> pd.DataFrame:
    df = forecast_df.merge(inventory_df, on=["sku", "location"], how="left")
    df = df.merge(suppliers_df, on="sku", how="left")

    df["expected_need_during_lead_time"] = (df["avg_daily_qty"] * df["lead_time_days"]).round(0)
    df["raw_reorder_qty"] = (df["expected_need_during_lead_time"] - df["on_hand"]).clip(lower=0)

    # apply MOQ when reorder is needed
    df["reorder_qty"] = df.apply(
        lambda row: max(row["raw_reorder_qty"], row["moq"]) if row["raw_reorder_qty"] > 0 else 0,
        axis=1,
    )
    df["reorder_value"] = (df["reorder_qty"] * df["unit_cost"]).round(2)

    df["urgency"] = df.apply(
        lambda row: "High" if row["on_hand"] < row["avg_daily_qty"] * 3
        else "Medium" if row["on_hand"] < row["avg_daily_qty"] * 7
        else "Low",
        axis=1,
    )
    return df
