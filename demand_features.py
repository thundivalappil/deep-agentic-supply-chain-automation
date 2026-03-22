import pandas as pd


def build_demand_features(sales: pd.DataFrame) -> pd.DataFrame:
    df = sales.copy()
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values(["sku", "location", "date"])

    grouped = df.groupby(["sku", "location", "date"], as_index=False)["qty"].sum()
    grouped["day_of_week"] = grouped["date"].dt.dayofweek
    grouped["month"] = grouped["date"].dt.month
    grouped["lag_1"] = grouped.groupby(["sku", "location"])["qty"].shift(1).fillna(0)
    grouped["rolling_mean_3"] = (
        grouped.groupby(["sku", "location"])["qty"]
        .rolling(3)
        .mean()
        .reset_index(level=[0, 1], drop=True)
        .fillna(grouped["qty"])
    )
    return grouped
