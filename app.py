from pathlib import Path

from src.ingestion.load_csv import load_sales_data, load_inventory_data, load_suppliers_data
from src.ingestion.validate_data import validate_inputs
from src.features.demand_features import build_demand_features
from src.forecasting.predict_forecast import run_forecast
from src.optimization.reorder_optimizer import optimize_reorder
from src.agents.orchestrator import run_agentic_orchestration
from src.outputs.export_json import export_results
from src.outputs.export_csv import export_dataframe

OUTPUT_DIR = Path("data/processed")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    sales = load_sales_data("data/sample/sales.csv")
    inventory = load_inventory_data("data/sample/inventory.csv")
    suppliers = load_suppliers_data("data/sample/suppliers.csv")

    validate_inputs(sales, inventory, suppliers)

    feature_df = build_demand_features(sales)
    forecast_df = run_forecast(feature_df)
    reorder_plan_df = optimize_reorder(forecast_df, inventory, suppliers)

    result = run_agentic_orchestration(
        forecast_df=forecast_df,
        inventory_df=inventory,
        suppliers_df=suppliers,
        plan_df=reorder_plan_df,
    )

    export_dataframe(reorder_plan_df, OUTPUT_DIR / "reorder_plan.csv")
    export_results(result, OUTPUT_DIR / "final_output.json")

    print("Deep Agentic Supply Chain pipeline completed successfully.")


if __name__ == "__main__":
    main()
