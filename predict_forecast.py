import pandas as pd


def run_forecast(feature_df: pd.DataFrame) -> pd.DataFrame:
    # Simple baseline for showcase publishing
    result = (
        feature_df.groupby(["sku", "location"], as_index=False)
        .agg(
            forecast_qty=("rolling_mean_3", "mean"),
            avg_daily_qty=("qty", "mean"),
        )
    )
    result["forecast_qty"] = result["forecast_qty"].round(0).astype(int)
    result["avg_daily_qty"] = result["avg_daily_qty"].round(2)
    return result
